# Python 3.9 기반 이미지 사용
FROM python:3.9

# 컨테이너 내부에서 실행할 디렉토리 설정
WORKDIR /app

# 환경 변수 설정 (Python 출력을 버퍼링하지 않도록 설정)
ENV PYTHONUNBUFFERED=1

# requirements.txt 복사 및 패키지 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . /app/

# 포트 설정 (Django 기본 포트: 8000)
EXPOSE 8000

# 실행 명령 (마이그레이션 후 서버 실행)
CMD ["sh", "-c", "python manage.py migrate && gunicorn --bind 0.0.0.0:8000 danny_community.wsgi:application"]
