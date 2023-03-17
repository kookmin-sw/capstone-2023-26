import cv2
import video_capture


def test_func(frame):
    global video_capture

    cv2.imshow('frame', frame) # frame 정보를 창에 띄워보고 싶으면 해당 코드 실행
    # print(frame) # frame에 대한 정보를 받아와서 활용하고 싶으면 해당 코드 실행

    # 해당 코드가 아직 싱글 스레드로 동작하고 있기에, 직접 해당 기능을 종료시키는 코드를 넣어야 다음 코드로 진행 가능.
    # video_capture의 stop_capturing()이 해당 기능을 담당함
    if cv2.waitKey(1) & 0xFF == 27: # esc키 누르면 종료
        video_capture.stop_capturing()


# global video_capture
video_capture = video_capture.VideoCapture()

"""
load_cam(1): 맥 기준 웹캠 로딩
locd_cam(0): 아이폰을 맥과 케이블로 연결한 후, 0번 값을 주고 실행하면 폰이랑 연결됨

"""
video_capture.load_cam(1)

print(video_capture.get_frame_info())
video_capture.start_capturing(test_func)