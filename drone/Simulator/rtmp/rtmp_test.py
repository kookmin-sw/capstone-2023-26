# import pyrtmp
# import subprocess

# def send_video_to_rtmp_server(file_path, rtmp_url):
#     # RTMP 연결 생성
#     rtmp_client = pyrtmp.RtmpClient(rtmp_url)
#     pyrtmp.rtmp

#     # 비디오 파일을 ffmpeg을 사용하여 읽고 RTMP 서버로 스트리밍
#     ffmpeg_cmd = ['ffmpeg', '-re', '-i', file_path, '-c:v', 'copy', '-f', 'flv', rtmp_url]
#     ffmpeg_process = subprocess.Popen(ffmpeg_cmd)

#     # RTMP 연결 시작
#     rtmp_client.connect()
#     rtmp_client.play("stream_name")

#     # ffmpeg 프로세스가 종료될 때까지 대기
#     ffmpeg_process.wait()

#     # RTMP 연결 종료
#     rtmp_client.close()

# # 실행 예시
# mp4_file = "video.mp4"
# rtmp_url = "rtmps://540f41fc71d9.global-contribute.live-video.net:443/app/sk_ap-northeast-2_ZMDMCLMyhdc5_X8OUmvrFwVhJWz0vBmTwzxGaASpeLL"
# send_video_to_rtmp_server(mp4_file, rtmp_url)

# import subprocess

# def send_video_to_server(video_path):
#     command = f"ffmpeg -re -i {video_path} -c copy -f flv -movflags frag_keyframe+empty_moov rtmps://540f41fc71d9.global-contribute.live-video.net:443/app/sk_ap-northeast-2_ZMDMCLMyhdc5_X8OUmvrFwVhJWz0vBmTwzxGaASpeLL"
#     subprocess.call(command.split())

# mp4_file = "video.mp4"
# send_video_to_server(mp4_file)

import subprocess

def send_video_to_rtmp_server(file_path, rtmp_url):
    # FFmpeg을 사용하여 mp4 파일을 RTMP 서버로 스트리밍
    ffmpeg_cmd = [
        'ffmpeg', '-re', '-i', file_path, '-c:v', 'copy', '-f', 'flv', rtmp_url
    ]
    subprocess.call(ffmpeg_cmd)
    print('streaming ended')

# 실행 예시
mp4_file = "output.mp4"
rtmp_url = "rtmps://540f41fc71d9.global-contribute.live-video.net:443/app/sk_ap-northeast-2_ZMDMCLMyhdc5_X8OUmvrFwVhJWz0vBmTwzxGaASpeLL"
send_video_to_rtmp_server(mp4_file, rtmp_url)