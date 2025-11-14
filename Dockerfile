# Python 기반 이미지 사용
FROM python:3.12-slim

# 컨테이너 안에서 작업할 디렉토리 지정
WORKDIR /app

# requirements.txt 복사해서 설치
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 전체 복사
COPY . .

# 장고 서버 포트 개방
EXPOSE 8000

# 장고 서버 실행 명령
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
