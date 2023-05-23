from django.shortcuts import render
import os
import subprocess
import datetime

# Create your views here.

def download_convert_upload():
    now = datetime.datetime.now()

    command = 'aws s3 cp s3://ivs-ditto/ivs/v1/392988993234/eknAgsglpDNs/2023/5/12/ . --exclude "*" --include "**/160p30/*.ts" --recursive'
    subprocess.run(command, shell=True, check=True)

    folder_path = "raw_data"  # 대상 폴더 경로를 지정해주세요
    output_file = f"{now.year}.{now.month}.{now.day}.mp4"  # 합쳐진 mp4 파일의 이름을 지정해주세요

    ts_files = [f for f in os.listdir(folder_path) if f.endswith(".ts")]
    ts_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))

    # .ts 파일 경로 목록 생성
    ts_file_paths = [os.path.join(folder_path, f) for f in ts_files]

    # .ts 파일들을 합쳐서 .mp4 파일로 변환
    command = ["ffmpeg", "-i", "concat:" + "|".join(ts_file_paths), "-c:v", "copy", "-c:a", "copy", output_file]
    subprocess.call(command)

    print("변환 완료")