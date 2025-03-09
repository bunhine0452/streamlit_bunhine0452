# 내 포트폴리오 웹사이트

Streamlit을 사용한 개인 PR 포트폴리오 웹사이트입니다. 프로필 정보, 기술 스택, 프로젝트 경험 및 블로그 포스팅을 한 곳에서 볼 수 있는 인터랙티브한 웹사이트입니다.

## 설치 방법

```bash
# 저장소 클론
git clone https://github.com/bunhine0452/streamlit_bunhine0452.git
cd streamlit_bunhine0452

# 필요한 패키지 설치
pip install -r requirements.txt
```

## 실행 방법

```bash
streamlit run main.py
```

## 주요 기능

- **반응형 디자인**: 모든 디바이스에서 최적화된 화면 제공
- **라이트 모드 강제 적용**: 다크 모드 사용자에게도 일관된 디자인 제공
- **프로필 섹션**: 전문적인 자기소개 및 개인 정보 표시
- **기술 스택**: 핵심 기술 및 역량을 시각적으로 표현
- **타임라인**: 교육 및 경력 이력을 타임라인 형태로 표시
- **프로젝트 갤러리**: 3열 그리드 레이아웃으로 주요 프로젝트 전시
- **블로그 섹션**: velog.io 블로그 포스팅 자동 가져오기 및 표시
  - 페이지네이션 기능으로 모든 블로그 포스트 탐색 가능
  - 커스텀 제목과 카드 디자인으로 직관적인 UI 제공

## 기술 스택

- **Frontend**: HTML, CSS, Streamlit
- **Backend**: Python
- **데이터 처리**: Pandas, NumPy
- **웹 스크래핑**: Requests, BeautifulSoup4, lxml
- **시각화**: Matplotlib, Plotly

## 폴더 구조

```
streamlit_bunhine0452/
├── main.py           # 메인 애플리케이션 파일
├── html_components.py # HTML 컴포넌트 정의
├── requirements.txt  # 의존성 패키지 목록
├── README.md         # 문서
├── img/              # 이미지 파일
└── pages/            # 블로그 포스트 페이지
```

## 참고 사항

- 이 웹사이트는 Streamlit 1.26.0 버전을 기준으로 개발되었습니다.
- 다양한 브라우저와 디바이스에서 테스트되었습니다.
- 블로그 포스팅은 velog.io 웹사이트에서 실시간으로 가져옵니다.