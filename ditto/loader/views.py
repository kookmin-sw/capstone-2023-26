from django.shortcuts import render
import os
import subprocess
import datetime
import requests
import json
# Create your views here.

def reUpload():
    now = datetime.datetime.now()

    command = 'aws s3 cp s3://ivs-ditto/ivs/v1/392988993234/eknAgsglpDNs/2023/5/12/ ./videostorage --exclude "*" --include "**/160p30/*.ts" --recursive'
    subprocess.run(command, shell=True, check=True)

    command = 'find ./videostorage -type f -name "*.ts" -exec sh -c \'mv "$0" "./videostorage/$(date -r "$0" +"%Y%m%d%H%M%S").ts"\' {} \\;'
    subprocess.run(command, shell=True, check=True)

    print("다운로드 완료")

    folder_path = "./videostorage"  # 대상 폴더 경로를 지정해주세요
    output_file = f"./videostorage/{now.year}.{now.month}.{now.day}.mp4"  # 합쳐진 mp4 파일의 이름을 지정해주세요

    ts_files = [f for f in os.listdir(folder_path) if f.endswith(".ts")]
    ts_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))

    # .ts 파일 경로 목록 생성
    ts_file_paths = [os.path.join(folder_path, f) for f in ts_files]

    # .ts 파일들을 합쳐서 .mp4 파일로 변환
    command = ["ffmpeg", "-i", "concat:" + "|".join(ts_file_paths), "-c:v", "copy", "-c:a", "copy", output_file]
    subprocess.run(command, check=True)

    print("변환 완료")

    command = f'aws s3 cp 2023.5.23.mp4 s3://ivs-ditto/ivs/v1/392988993234/eknAgsglpDNs/2023/5/12/'

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    output = output.decode('utf-8')

    key_value = output.split(' ')[-1].strip()
    print("output:", output)
    print("uploaded key:", key_value)

    print("업로드 완료")

    url = 'http://127.0.0.1:8000/api/recordinglog/'

    data = {
                "time": f'{now}',
                "s3key": f'{key_value}',
                "event_id": 1
            }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, headers={"Content-Type": "application/json"})

    if response.status_code == 201:
        print("post!")
    else:
        print('fail')
        
reUpload()