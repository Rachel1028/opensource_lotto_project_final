🎲 **OpenSource Lotto Project (Django + Docker)**
개발 환경: macOS · VSCode · Python 3.12 · Django 5.1.4 · Docker

🧩 **프로젝트 소개**
OpenSource Lotto Project는 사용자 로또 구매, 관리자 당첨 추첨, 결과 확인 기능을 모두 포함한
로또 웹 서비스입니다.
Django 기반으로 구현되었으며, Docker를 활용해 실행 환경을 통일하여
어디서나 동일한 환경으로 실행할 수 있습니다.

**🌟 제공 기능 요약**
**👤 사용자 기능**
1) 🎰 로또 구매 (수동/자동)
수동: 사용자가 직접 번호 6개 입력
자동: 1~45 중 랜덤 6개 번호 자동 생성
구매 시 이름 등록 가능
모든 구매 데이터는 DB에 저장됨

**3) 📋 구매 내역 조회**
메인 페이지에서 지금까지 구매한 모든 티켓 확인
티켓 목록에 구매자 이름 + 번호 조합이 표시됨
최신순 정렬로 최근 구매를 바로 확인 가능

**5) 🏆 당첨 결과 확인**
관리자가 추첨한 가장 최근 당첨 번호와 비교
내가 맞춘 개수에 따라 자동 등수 부여
맞춘 개수	등급	표시
6개	🥇 1등	빨간색 강조
5개	🥈 2등	파란색 강조
4개	🥉 3등	회색 강조
3개 이하	꽝	표시 없음
등수와 함께 맞춘 번호 개수도 바로 확인 가능

**🛠 관리자 기능**
**1) 🎯 당첨 번호 추첨**
관리자 페이지에서 당첨 번호 6개 생성
추첨 번호는 DB에 저장되고 사용자 당첨 확인에 사용됨
시간 기준으로 최신 번호가 자동으로 사용됨

**3) 📊 판매 내역 확인**
모든 사용자 구매 티켓 목록 조회
구매 시간, 입력 번호, 사용자 이름 확인 가능
필터/정렬 기능을 통해 원하는 데이터만 조회 가능

**5) 👑 당첨자 관리**
사용자 구매 티켓과 당첨 번호 비교
관리자는 어떤 사용자가 몇 개를 맞췄는지 한눈에 파악 가능
당첨자의 번호와 등급도 확인 가능

**🗂 전체 구조**
opensource_lotto/
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── db.sqlite3
│
├── opensource_lotto/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── lotto/
    ├── admin.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── templates/
        ├── home.html
        ├── buy.html
        ├── result.html
        └── winners.html
        
**▶️ 실행 방법**
**🐍 로컬 (venv) 실행**
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver

**접속 링크: http://127.0.0.1:8000/**

**🐳 Docker 실행**
docker compose up --build
접속 링크: http://localhost:8000/

**🧰 Docker 명령어 정리**
**명령	기능**
docker compose up --build	컨테이너 빌드 및 실행
docker compose down	컨테이너 종료
docker ps	실행 중인 컨테이너 조회
docker logs [ID]	특정 컨테이너 로그 확인
docker image ls	이미지 목록 조회

**👩‍💻 프로젝트 특징**
✔️ 1. 사용자 흐름이 명확한 UI/UX 구조
메인 → 구매하기 → 결과확인 흐름이 자연스러움
번호 입력 UI 크게 개선하여 가독성 향상
당첨 결과는 즉시 확인 가능

**✔️ 2. 관리자 기능 완전 분리**
일반 사용자 접근 불가
관리자 페이지에서 모든 번호 및 데이터 관리

**✔️ 3. Docker 기반 실행**
팀 프로젝트에 적합
어디서 실행해도 동일한 환경 보장

**📚 참고 문헌**
Django 공식 문서
Docker 공식 문서
Python random 라이브러리
HTML/CSS 디자인 참고

**✨ 개발자 정보**
Heo Yunseo (허윤서)
GitHub: https://github.com/Rachel1028
Repository: https://github.com/Rachel1028/opensource_lotto_project_final
