from map.models import HeadCount, CountHistory
from events.models import Event
from django.db.models import Sum
from datetime import datetime
import os
import subprocess
import json
import requests
from urllib import parse

def updateCountHistory():
    print(datetime.now())
    headcounts = HeadCount.objects.values("event_id").annotate(Sum('count'))
    print(len(headcounts))
    for headcount in headcounts:
        print(datetime.now())
        history = CountHistory(count=headcount["count__sum"])
        history.event_id = Event.objects.get(id=headcount["event_id"])
        history.save()
        
def reUpload():
    current_dir = os.path.abspath(__file__)
    target_dir = os.path.dirname(current_dir) + '/videostorage'

    now = datetime.now()
    print(f'target_dir: {target_dir}')
    print(now)
    
    #print('========================== Download Process Start ==========================')
    ## 특정일 폴더 하위의 ts파일을 폴더 구조를 유지한 채로 복사
    #command = f'aws s3 cp s3://ivs-ditto/ivs/v1/392988993234/eknAgsglpDNs/2023/5/12/ {target_dir} --exclude "*" --include "**/160p30/*.ts" --recursive'
    #try:
    #    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #    print('s3 download success')
    #except:
    #    print('s3 download fail')
    #output, error = process.communicate()
    #print(error)
    
    #print('========================== Download Process Done ==========================')

    print('========================== Sorting Process Start ==========================')
    # ts파일들을 폴더 구조를 파괴하며 시간순으로 정렬하여 옮김
    command = f'find {target_dir} -type f -name "*.ts" -exec sh -c \'mv "$0" "{target_dir}/$(date -r "$0" +"%Y%m%d%H%M%S").ts"\' {{}} \\;'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()    
    print(error)

    folder_path = target_dir  # 대상 폴더 경로를 지정해주세요
    output_file = f"{target_dir}/{now.year}.{now.month}.{now.day}.mp4"  # 합쳐진 mp4 파일의 이름을 지정해주세요

    ts_files = [f for f in os.listdir(folder_path) if f.endswith(".ts")]
    ts_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
    print('========================== Sorting Process Done ==========================')

    print('========================== Conversion Process Start ==========================')
    # ts 파일 경로 목록 생성
    ts_file_paths = [os.path.join(folder_path, f) for f in ts_files]

    # ts 파일들을 합쳐서 .mp4 파일로 변환
    command = ["ffmpeg", "-i", "concat:" + "|".join(ts_file_paths), "-c:v", "copy", "-c:a", "copy", output_file]
    subprocess.run(command, check=True)
    
    print('========================== Conversion Process Done ==========================')

    print('========================== S3 Upload Process Start ==========================')
    # mp4파일을 s3에 재업로드 하고 그 객체에 접근하기 위한 key값을 가져옴
    command = f'aws s3 cp {target_dir}/{now.year}.{now.month}.{now.day}.mp4 s3://ivs-ditto/ivs/v1/392988993234/eknAgsglpDNs/2023/5/12/'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    deoutput = output.decode('utf-8')
    print(error)
    
    print('========================== S3 Upload Process Done ==========================')
    
    print('========================== Local Process Start ==========================')

    key_value = deoutput.split(' ')[-1].strip()
    print("output:", deoutput)
    print("uploaded key:", key_value)
    
    # url 인코딩
    s3key = parse.quote(key_value)

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
        print('local upload success')
    else:
        print('local upload fail')
        
    print('========================== Local Process Done ==========================')
                
    print('========================== Delete Process Start ==========================')             
    # videostorage의 파일들 전부 삭제
    command = ['find', target_dir + '/*', '-delete']
    command = ['rm', '-rf', target_dir]
    try:
        subprocess.run(command, check=True)
        print('delete success')
    except:
        print('delete fail')
    print('========================== Delete Process Done ==========================')