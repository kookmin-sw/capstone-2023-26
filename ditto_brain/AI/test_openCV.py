import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print("Unable to read camera")
    
else:

    # 프레임의 정보 가져와 변수에 저장한다. 
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))


    #캠으로 들어온 비디오를 따로 저장한다.
    out = cv2.VideoWriter('data/videos/output.avi',
                        cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                        10,
                        (frame_width, frame_height) )
                        
                        
    # 동영상은 사진을 여러장 이어서 보여주는 개념이다.
    # 1초에 몇 장의 이미지가 들어가는지, fps(frame per second) 단위를 쓴다.
    # 캠으로부터 이미지 한 장만을 받아올 게 아니므로, 반복문을 사용한다.
    while True:
        ret, frame = cap.read()
        if ret == True:
            out.write(frame)
            cv2.imshow('frame', frame)
			#esc를 입력하면, 이미지를 받아오길 멈추게 한다.
            if cv2.waitKey(1) & 0xFF == 27:
                break
        else:
            break
            
            
    # sql 커서와 커넥션을 다 사용하고 나면 연결을 닫아주듯이, 비디오캡쳐도 닫아준다.
    cap.release()
    # 파일도 더 이상 작성하지 않도록 한다.
    out.release()
    
 	#화면에 띄운 창을 닫아준다.
    cv2.destroyAllWindows()