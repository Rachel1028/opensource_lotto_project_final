🎲 Lotto Project (Django + Docker)
개발 환경: macOS · VSCode · Python 3.12 · Django 5.1.2 · Docker
🌱 프로젝트 개요
이 프로젝트는 Django 웹 프레임워크와 Docker를 활용하여
로또 번호 구매 및 조회가 가능한 간단한 웹사이트를 구축한 것입니다.
사용자는 수동 또는 자동으로 로또 번호를 구매할 수 있습니다.
구매한 번호는 SQLite 데이터베이스에 저장됩니다.
Docker를 사용해 개발 환경을 컨테이너로 통합하여 일관된 실행 환경을 제공합니다.
🧱 기술 스택
구분	사용 기술
Backend	Django 5.1.2 (Python)
Database	SQLite3
Container	Docker, Docker Compose
IDE	Visual Studio Code
OS	macOS
⚙️ 주요 기능
기능	설명
🎰 로또 번호 구매	사용자가 번호를 직접 입력(수동)하거나 자동 생성하여 구매
📋 구매 내역 확인	저장된 모든 구매 내역을 목록 형태로 확인
🧮 자동 번호 생성	random.sample()을 사용하여 1~45 사이의 숫자 6개 자동 생성
🎯 당첨 여부 확인 기능	최신 추첨 번호 기준으로 각 티켓의 맞은 숫자 수·등수 계산
🛠 관리자 페이지 제공	Django Admin에서 구매 티켓·추첨 번호 관리
🐳 Docker 실행 지원	docker compose up 명령으로 프로젝트 전체 실행 가능
🐳 Docker 실행 방법
1) Docker 빌드 및 실행
docker compose up --build
2) 브라우저 접속
http://localhost:8000/
3) Docker 종료
docker compose down
🖥 로컬 실행 방법 (Docker 없이)
1) 가상환경 생성 및 활성화
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
2) 패키지 설치
pip install -r requirements.txt
3) Django 개발 서버 실행
python3 manage.py runserver
✨ 작성자
Name: Heo Yunseo
GitHub: https://github.com/Rachel1028
프로젝트 저장소: https://github.com/Rachel1028/opensource_lotto_project_final.git
