#!/bin/bash

# 필요한 패키지 설치 확인
echo "필요한 패키지 설치 확인 중..."
pip install -r requirements.txt

# Streamlit 앱 실행
echo "포트폴리오 웹사이트 시작 중..."
streamlit run main.py 