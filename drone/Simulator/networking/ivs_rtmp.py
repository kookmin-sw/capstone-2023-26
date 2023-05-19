import subprocess

def send_video_to_rtmp_server(file_path, rtmp_url):
    # FFmpeg을 사용하여 mp4 파일을 RTMP 서버로 스트리밍
    ffmpeg_cmd = [
        'ffmpeg', '-re', '-i', file_path, '-c:v', 'copy', '-f', 'flv', rtmp_url
    ]
    subprocess.call(ffmpeg_cmd)
    print('streaming ended')

# 실행 예시
# send_video_to_rtmp_server(mp4_file, rtmp_url)