import matplotlib.pyplot as plt
import torch
import cv2
import math

from torchvision import transforms

import numpy as np
import os

import boto3

from utils.datasets import letterbox
from utils.general import non_max_suppression_kpt
from utils.plots import output_to_keypoint, plot_skeleton_kpts
from moviepy.video.io.VideoFileClip import VideoFileClip

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
weigths = torch.load('yolov7-w6-pose.pt')
model = weigths['model']
model = model.half().to(device)
_ = model.eval()

url = "https://540f41fc71d9.ap-northeast-2.playback.live-video.net/api/video/v1/ap-northeast-2.392988993234.channel.eknAgsglpDNs.m3u8"
cap = cv2.VideoCapture(url)

if (cap.isOpened() == False):
    print('Error while trying to read video. Please check path again')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

vid_write_image = letterbox(cap.read()[1], (frame_width), stride=64, auto=True)[0]
resize_height, resize_width = vid_write_image.shape[:2]

# 영상 저장
out = cv2.VideoWriter(f"result.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 30, (resize_width, resize_height))

frame_count = 0
total_fps = 0 

# AWS
ACCESS_KEY_ID = 'key_id'
ACCESS_SECRET_KEY = 'secret_key'
BUCKET_NAME = 'bucket_name'

def s3_connection():
    try:
        # s3 클라이언트 생성
        s3 = boto3.client(
            service_name="s3",
            region_name="ap-northeast-2",
            aws_access_key_id=ACCESS_KEY_ID,
            aws_secret_access_key=ACCESS_SECRET_KEY,
        )
    except Exception as e:
        print(e)
    else:
        print("s3 bucket connected!") 
        return s3
        
s3 = s3_connection()

while cap.isOpened():
    
    print("Frame {} Processing".format(frame_count))
    frame_count += 1
    
    ret, frame = cap.read()
    
    if ret:
 
        orig_image = frame

        image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB)
        image = letterbox(image, (frame_width), stride=64, auto=True)[0]
        image_ = image.copy()
        image = transforms.ToTensor()(image)
        image = torch.tensor(np.array([image.numpy()]))
                
        image = image.half().to(device)  
        
        with torch.no_grad():
            output, _ = model(image)
            
        output = non_max_suppression_kpt(output, 0.25, 0.65, nc=model.yaml['nc'], nkpt=model.yaml['nkpt'], kpt_label=True)
        output = output_to_keypoint(output)
        im0 = image[0].permute(1, 2, 0) * 255
        im0 = im0.cpu().numpy().astype(np.uint8)
        
        im0 = cv2.cvtColor(im0, cv2.COLOR_RGB2BGR)
        
        for idx in range(output.shape[0]):
            plot_skeleton_kpts(im0, output[idx, 7:].T, 3)
            xmin, ymin = (output[idx, 2]-output[idx, 4]/2), (output[idx, 3]-output[idx, 5]/2)
            xmax, ymax = (output[idx, 2]+output[idx, 4]/2), (output[idx, 3]+output[idx, 5]/2)

            left_shoulder_y= output[idx][23]
            left_shoulder_x= output[idx][22]
            right_shoulder_y= output[idx][26]
            
            left_body_y = output[idx][41]
            left_body_x = output[idx][40]
            right_body_y = output[idx][44]

            len_factor = math.sqrt(((left_shoulder_y - left_body_y)**2 + (left_shoulder_x - left_body_x)**2 ))

            left_foot_y = output[idx][53]
            right_foot_y = output[idx][56]
            
            if left_shoulder_y > left_foot_y - len_factor and left_body_y > left_foot_y - (len_factor/2) and left_shoulder_y > left_body_y - (len_factor/2):

                cv2.rectangle(im0, (int(xmin), int(ymin)), (int(xmax), int(ymax)), color=(255, 255, 255), thickness=5, lineType=cv2.LINE_AA)
                cv2.putText(im0, 'Fall Down Detected', (11, 100), 0, 1, [0, 0, 255], thickness=2, lineType=cv2.LINE_AA)
                # filename = "savedImage.jpg"
                
                '''
                S3로 영상을 보내는 코드 구현 부분
                '''
                # 로컬 디렉토리에 동영상 저장
                cv2.imshow('video', im0)
                out.write(im0)
                
                video = VideoFileClip('result.mp4')
                duration = video.duration
                
                # 10초보다 크면 10초로 자른 영상 저장
                # 그렇지 않다면 그냥 영상 저장
                if duration > 10: 
                    cut_video = video.subclip((duration - 10), duration)
                
                cut_video.write_videofile('result.mp4')
                
                # s3로 해당 영상 업로드
                try:
                    s3.upload_file('result.mp4', BUCKET_NAME, "{버킷에 저장될 파일 이름}")
                except Exception as e:
                    print(e)
                                
                # cv2.imwrite(filename, im0)
                # os.remove(filename)
       
        # cv2.imshow('image', im0)
        # out.write(im0)

        if cv2.waitKey(1) & 0xFF == ord('q'):
             break
            
    else:
        break

cap.release()
cv2.destroyAllWindows()

