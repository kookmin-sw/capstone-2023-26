from django.shortcuts import render
import os
import subprocess
import datetime
import requests
import json
from urllib import parse
# Create your views here.

def reUpload():
    current_dir = os.path.abspath(__file__)
    target_dir = os.path.dirname(current_dir) + '/videostorage'

    now = datetime.datetime.now()

    # 특정일 폴더 하위의 ts파일을 폴더 구조를 유지한 채로 복사
    command = f'aws s3 cp s3://ivs-ditto/ivs/v1/392988993234/eknAgsglpDNs/2023/5/12/ {target_dir} --exclude "*" --include "**/160p30/*.ts" --recursive'
    try:
        subprocess.run(command, shell=True, check=True)
    except:
        print('s3 download error')

    # ts파일들을 폴더 구조를 파괴하며 시간순으로 정렬하여 옮김
    command = f'find {target_dir} -type f -name "*.ts" -exec sh -c \'mv "$0" "{target_dir}/$(date -r "$0" +"%Y%m%d%H%M%S").ts"\' {{}} \\;'
    try:
        subprocess.run(command, shell=True, check=True)
    except:
        print('sorting error')
        
    print("다운로드 완료")

    folder_path = target_dir  # 대상 폴더 경로를 지정해주세요
    output_file = f"{target_dir}/{now.year}.{now.month}.{now.day}.mp4"  # 합쳐진 mp4 파일의 이름을 지정해주세요

    ts_files = [f for f in os.listdir(folder_path) if f.endswith(".ts")]
    ts_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))

    # ts 파일 경로 목록 생성
    ts_file_paths = [os.path.join(folder_path, f) for f in ts_files]

    # ts 파일들을 합쳐서 .mp4 파일로 변환
    command = ["ffmpeg", "-i", "concat:" + "|".join(ts_file_paths), "-c:v", "copy", "-c:a", "copy", output_file]
    try:
        subprocess.run(command, check=True)
    except:
        print('conversion error')

    print("변환 완료")

    # mp4파일을 s3에 재업로드 하고 그 객체에 접근하기 위한 key값을 가져옴
    command = f'aws s3 cp {target_dir}/{now.year}.{now.month}.{now.day}.mp4 s3://ivs-ditto/ivs/v1/392988993234/eknAgsglpDNs/2023/5/12/'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    deoutput = output.decode('utf-8')

    key_value = deoutput.split(' ')[-1].strip()
    print("output:", deoutput)
    print("uploaded key:", key_value)
    
    # url 인코딩
    s3key = parse.quote(key_value)

    print("업로드 완료")

    url = 'http://127.0.0.1:8000/api/recordinglog/'

    data = {
                "time": f'{now}',
                "s3key": f'{s3key}',
                "event_id": 1
            }

    json_data = json.dumps(data)

    # 데이터베이스에 영상의 날짜와 접근하기위한 key 저장
    response = requests.post(url, data=json_data, headers={"Content-Type": "application/json"})

    if response.status_code == 201:
        print("post!")
    else:
        print('fail')
        
    # videostorage의 파일들 전부 삭제
    command = ['rm', '-rf', target_dir]
    subprocess.run(command, check=True)
        
reUpload()