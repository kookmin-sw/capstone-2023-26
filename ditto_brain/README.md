# ditto_brain 모듈
해당 모듈은 드론의 비행 데이터 수집 후 가공을 거친 후, 다른 모듈에 결과물을 전달하는 역할을 합니다.

## 정보
- Python: 3.9.12

## 사용법
ditto_brain 모듈로 경로를 이동한 후, 아래와 같은 절차를 따릅니다.
### 가상환경 실행
가상환경 실행:
```
source venv/bin/activate
```
종료할 시에는 아래와 같이 입력합니다.
가상환경 종료:
```
deactivate
```

### requirements
서로의 작업 환경을 맞추기 위해서 requirements를 사용합니다.

requirements 설치:
```
pip install -r requirements.txt
```

requirements 내보내기:
```
pip freeze > requirements.txt
```
