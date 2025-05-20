폴더구조_ 라즈베리파이

/home/jg_jeong/water-temp-project/
├── sensor/                  # 수온 센서 측정 모듈
│   ├── __init__.py
│   ├── read_temp.py         # 온도 읽기 함수
│   ├── requirements.txt     # w1thermsensor 등
│   └── tests/               # (옵션) 유닛테스트
│       └── test_read.py
│
├── crawler/                 # 웹 크롤링 모듈
│   ├── __init__.py
│   ├── crawler.py           # 크롤러 로직
│   └── requirements.txt     # requests, BeautifulSoup 등
│
├── data/                    # 측정값·크롤링 데이터 저장소
│   ├── temp.csv             # 수온 로그
│   └── crawl_data.json      # 크롤링 결과 (예시)
│
├── server/                  # API 서버 (Flask / FastAPI 등)
│   ├── __init__.py
│   ├── app.py               # REST 엔드포인트
│   └── requirements.txt
│
├── venv/                    # (선택) 가상환경
│
└── README.md


이 프로젝트는 웨이브파크의 수온을 측정하고 축증한 수온을 웹 으로 보여주기 위한 프로그래밍입니다.

언어는 Python으로 작성 되었으며, 서버는 라즈베리파이로 API를 프론트에 보내주기 위해 작성되었습니다.
라즈베리파이 공식 홈페이지의 온도센서 측정을 참고하였으머, 온도 측정 센서는 DS18B20 을 사용하였습니다.
