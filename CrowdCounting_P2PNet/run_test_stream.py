# -*- coding: utf-8 -*-
# +
import argparse
import datetime
import random
import time
import pandas as pd
from pathlib import Path

import torch
import torchvision.transforms as standard_transforms
import numpy as np

from PIL import Image
import cv2
from crowd_datasets import build_dataset
from engine import *
from models import build_model
import os
import warnings
warnings.filterwarnings('ignore')

def get_args_parser():
    parser = argparse.ArgumentParser('Set parameters for P2PNet evaluation', add_help=False)
    
    # * Backbone
    parser.add_argument('--backbone', default='vgg16_bn', type=str,
                        help="name of the convolutional backbone to use")

    parser.add_argument('--row', default=2, type=int,
                        help="row number of anchor points")
    parser.add_argument('--line', default=2, type=int,
                        help="line number of anchor points")

    parser.add_argument('--output_dir', default='./',
                        help='path where to save')
    parser.add_argument('--weight_path', default='./weights/SHTechA.pth',
                        help='path where the trained weights saved')

    parser.add_argument('--gpu_id', default=0, type=int, help='the gpu used for evaluation')

    return parser

def main(args, debug=False):
    start=time.time()

    os.environ["CUDA_VISIBLE_DEVICES"] = '{}'.format(args.gpu_id)

    print(args)
    device = torch.device('cuda')
    # get the P2PNet
    model = build_model(args)
    # move to GPU
    model.to(device)
    # load trained model
    if args.weight_path is not None:
        checkpoint = torch.load(args.weight_path, map_location='cpu')
        model.load_state_dict(checkpoint['model'])
    # convert to eval mode
    model.eval()
    # create the pre-processing transform
    transform = standard_transforms.Compose([
        standard_transforms.ToTensor(), 
        standard_transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    url = "https://889962c23ee6.ap-northeast-2.playback.live-video.net/api/video/v1/ap-northeast-2.196202674046.channel.ppLGhcD0q6ZR.m3u8"
    cap=cv2.VideoCapture(url)
    fourcc = cv2.VideoWriter_fourcc(*'FMP4')
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH) #원본 동영상 크기 정보 받아옴
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    out = cv2.VideoWriter('output.mp4', fourcc, 30, (int(w//128*128),int(h//128*128)))
    
    while True:
      hasFrame, img_frame=cap.read() #프레임 읽어옴
      if not hasFrame: #더이상 받아올 프레임 없는 경우
        break
      
      img_raw = Image.fromarray(img_frame).convert('RGB')
      # round the size
      width, height = img_raw.size
      new_width = width // 128 * 128
      new_height = height // 128 * 128
      img_raw = img_raw.resize((new_width, new_height), Image.ANTIALIAS)
      # pre-proccessing
      img = transform(img_raw)

      samples = torch.Tensor(img).unsqueeze(0)
      samples = samples.to(device)
      # run inference
      outputs = model(samples)
      outputs_scores = torch.nn.functional.softmax(outputs['pred_logits'], -1)[:, :, 1][0]

      outputs_points = outputs['pred_points'][0]

      threshold = 0.5
      # filter the predictions
      points = outputs_points[outputs_scores > threshold].detach().cpu().numpy().tolist()
      predict_cnt = int((outputs_scores > threshold).sum())

      outputs_scores = torch.nn.functional.softmax(outputs['pred_logits'], -1)[:, :, 1][0]

      outputs_points = outputs['pred_points'][0]
      # draw the predictions
      size = 5
      img_to_draw = cv2.cvtColor(np.array(img_raw), cv2.COLOR_RGB2BGR)
      for p in points:
          img_to_draw = cv2.circle(img_to_draw, (int(p[0]), int(p[1])), size, (0, 0, 255), -1)
      img_to_draw=cv2.cvtColor(np.array(img_to_draw), cv2.COLOR_BGR2RGB)
      out.write(img_to_draw)

      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      
      if predict_cnt>=5:
        print(predict_cnt)
        
        outputs_df = pd.DataFrame(points, columns=['width', 'height'])
        outputs_df.to_csv('tmp_points.csv', encoding='utf-8')

    print("original size: ", width, height)
    print("resized size: ", new_width, new_height)
    
    cap.release()
    out.release()
    print(time.time()-start)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('P2PNet evaluation script', parents=[get_args_parser()])
    args = parser.parse_args()
    main(args)
# -


