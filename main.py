import streamlit as st
import base64
from html_components import add_fontawesome, timeline_item, skill_progress_bar, card,social_media_icon
from PIL import Image
import random
import os
from datetime import datetime
import streamlit.components.v1 as components
import webbrowser
import requests
from bs4 import BeautifulSoup
import re
import lxml.html


# 페이지 설정
st.set_page_config(
    page_title="내 포트폴리오",
    page_icon="👨‍💻",
    layout="wide"
)

# 다크모드에서도 라이트모드로 표시되도록 강제 설정
st.markdown("""
<style>
    /* 라이트모드 강제 적용 */
    .stApp {
        background-color: white;
        color: black;
    }

</style>
""", unsafe_allow_html=True)

# CSS 스타일 정의
def local_css():
    st.markdown("""
    <style>
        /* 글꼴 설정 */
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap');
        
        * {
            font-family: 'Noto Sans KR', sans-serif;
        }
        
        /* 헤더 스타일 */
        .header-container {
            display: flex;
            align-items: center;
            padding: 2rem 0;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .profile-image {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            object-fit: cover;
            border: 5px solid white;
            margin: 0 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .header-text {
            color: white;
        }
        
        .header-text h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        
        .header-text h3 {
            font-size: 1.3rem;
            font-weight: 300;
            opacity: 0.9;
        }
        
        /* 섹션 스타일 */
        .section {
            background-color: white;
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        
        .section h2 {
            color: #764ba2;
            border-bottom: 2px solid #764ba2;
            padding-bottom: 0.5rem;
            margin-bottom: 1rem;
        }
        
        /* 스킬 배지 스타일 */
        .skill-badge {
            display: inline-block;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            margin: 0.3rem;
            font-size: 0.9rem;
        }
        
        /* 프로젝트 카드 스타일 */
        .project-card-link {
            text-decoration: none;
            color: inherit;
            display: block;
            cursor: pointer;
        }
        
        .project-card {
            border: 1px solid #eee;
            border-radius: 10px;
            padding: 1.2rem;
            margin-bottom: 1rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            height: 100%;
            display: flex;
            flex-direction: column;
            background-color: white;
            position: relative;
        }
        
        .project-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .project-card:after {
            content: "→";
            position: absolute;
            bottom: 12px;
            right: 15px;
            color: #764ba2;
            font-size: 1.2rem;
            font-weight: bold;
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .project-card:hover:after {
            opacity: 1;
        }
        
        .project-title {
            color: #764ba2;
            margin-bottom: 0.8rem;
            font-size: 1.2rem;
            line-height: 1.4;
            font-weight: 600;
        }
        
        .project-card img {
            border-radius: 5px;
            margin-bottom: 15px;
            width: 100%;
            height: 160px;
            object-fit: cover;
        }
        
        .project-content {
            flex-grow: 1;
            line-height: 1.5;
            margin-bottom: 20px;
        }
        
        .project-content p {
            margin-bottom: 12px;
            color: #333;
        }
        
        /* 프로젝트 기술 스택 태그 스타일 */
        .tech-tags {
            display: flex;
            flex-wrap: wrap;
            margin-top: 10px;
        }
        
        .tech-tag {
            display: inline-block;
            background-color: #f5f5f5;
            color: #555;
            padding: 4px 8px;
            border-radius: 4px;
            margin-right: 6px;
            margin-bottom: 6px;
            font-size: 12px;
        }
        
        /* 연락처 아이콘 스타일 */
        .contact-icons {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-top: 1rem;
        }
        
        .contact-icon {
            font-size: 1.5rem;
            color: #764ba2;
            transition: transform 0.3s ease;
        }
        
        .contact-icon:hover {
            transform: scale(1.2);
        }
        
        /* 타임라인 스타일 */
        .timeline {
            margin-left: 20px;
        }
        
        /* 반응형 디자인 */
        @media (max-width: 768px) {
            .header-container {
                flex-direction: column;
                text-align: center;
            }
            
            .profile-image {
                margin-bottom: 1rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)

def get_base64_of_image(image_path):
    """이미지를 base64로 인코딩하는 함수"""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def main():
    # CSS 적용
    local_css()
    # Font Awesome 추가
    add_fontawesome()
    # 소셜 미디어 아이콘 준비
    icons_html = ""
    icons_html += social_media_icon("github", "https://github.com/bunhine0452")
    icons_html += social_media_icon("chain", "https://solved.ac/profile/bunhine0452")
    icons_html += social_media_icon("pencil", "https://velog.io/@bunhine0452/")
    # 헤더 섹션
    st.markdown(f'''
    <div class="header-container">
        <img class="profile-image" src="https://github.com/bunhine0452.png" alt="프로필 이미지">
        <div class="header-text">
            <h1>김현빈</h1>
            <h3> AI 엔지니어 | </h3>
        </div>
        <div style="border-left: 2px solid white; height: 150px; margin: 0 1.5rem;"></div>
        <div style="color: white; line-height: 1.6;">
            <div style="margin-bottom: 10px;"><i class="fas fa-envelope" style="margin-right: 10px;"></i> <a href="mailto:hb000122@gmail.com" style="color: white; text-decoration: none;">hb000122@gmail.com</a></div>      
            <div style="margin-bottom: 10px;"><i class="fas fa-message" style="margin-right: 10px;"></i> <a href="https://open.kakao.com/o/sutz1Cjh" target="_blank" style="color: white; text-decoration: none;">https://open.kakao.com/o/sutz1Cjh</a></div>
            <div style="margin-bottom: 10px;"><i class="fas fa-map-marker-alt" style="margin-right: 10px;"></i> 서울시 동작구</div>
            <div style="display: flex; margin-top: 15px;">
                
                {icons_html}

    </div>
    ''', unsafe_allow_html=True)
    
    # 프로필 이미지로 변경
    # <img class="profile-image" src="data:image/png;base64,{get_base64_of_image('./img/profile.png')}" alt="프로필 이미지">
    # line167
    # <div style="margin-bottom: 10px;"><i class="fas fa-phone" style="margin-right: 10px;"></i> 010-5495-0452</div>
   
    # 3분할 레이아웃
    col1, col2, col3 = st.columns([1, 1, 1])
    
    # 자기소개 섹션
    with col1:
        st.markdown("""
        <div class="section">
            <h2>자기소개</h2>
            <p>
                어떻게 하면 생산적인 모델을 구현하는지 매일 고찰하는 개발자입니다.
                현재는 개발부터 서비스 모델 배포까지의 과정을 공부하고 있으며
                새로운 기술에 대해 매일 지식을 업데이트 중입니다.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # 스킬 섹션
        st.markdown('''
                    <div class="section">
                        <h2>기술 스택</h2>
                        <div class="skill-category">
                            <div class="category-title"></div>
                            <div class="skills-container">
                                <span class="skill-tag language-tag">🐍 Python</span>
                                <span class="skill-tag language-tag">🗃️ SQL</span>
                                <span class="skill-tag language-tag">📱 JavaScript</span>
                                <span class="skill-tag ml-tag">🔷 TensorFlow</span>
                                <span class="skill-tag ml-tag">🔥 PyTorch</span>
                                <span class="skill-tag ml-tag">📊 scikit-learn</span>
                                <span class="skill-tag ml-tag">🐼 pandas</span>
                                <span class="skill-tag ml-tag">🤖 LLM</span>
                                <span class="skill-tag ml-tag">💾 GGUF</span>
                                <span class="skill-tag ml-tag">📚 BERT</span>
                                <span class="skill-tag ml-tag">🎨 GAN</span>
                                <span class="skill-tag ml-tag">📷 U-Net</span>
                                <span class="skill-tag web-tag">📊 Streamlit</span>
                                <span class="skill-tag web-tag">🔮 Django</span>
                                <span class="skill-tag web-tag">🧪 Flask</span>
                                <span class="skill-tag ml-tag">🔍 OpenCV</span>
                                <span class="skill-tag ml-tag">🖼️ 이미지 처리</span>
                                <span class="skill-tag ml-tag">😀 감정 분석</span>
                                <span class="skill-tag ml-tag">💬 자연어 처리</span>
                                <span class="skill-tag tool-tag">📂 Git</span>
                                <span class="skill-tag tool-tag">🐳 Docker</span>
                                <span class="skill-tag tool-tag">☁️ AWS</span>
                                <span class="skill-tag tool-tag">🔄 CI/CD</span>
                                <span class="skill-tag tool-tag">📓 Jupyter</span>
                            </div>
                        </div>
                    </div>
                    ''', unsafe_allow_html=True)
        
        # 스킬 태그 스타일 정의
        st.markdown("""
        <style>
            .skills-container {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                margin-bottom: 15px;
            }
            
            .skill-category {
                margin-bottom: 20px;
            }
            
            .category-title {
                font-weight: 600;
                margin-bottom: 10px;
                color: #555;
                font-size: 16px;
            }
            
            .skill-tag {
                background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 8px 15px;
                border-radius: 20px;
                font-size: 14px;
                display: inline-block;
                margin-bottom: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }
            
            .skill-tag:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 8px rgba(0,0,0,0.15);
            }
        """, unsafe_allow_html=True)
        
    # 경력 섹션
    with col2:
        # st.markdown('<div class="section"><h2>경력</h2></div>', unsafe_allow_html=True)
        
        # # 타임라인 아이템 사용
        # timeline_html = ""
        # timeline_html += timeline_item("2020", "ABC 테크놀로지 - 선임 개발자", "웹 애플리케이션 개발 및 유지보수, 인공지능 모델 개발 및 배포, 주니어 개발자 멘토링")
        # timeline_html += timeline_item("2018", "XYZ 소프트웨어 - 주니어 개발자", "프론트엔드 개발, 사용자 인터페이스 개선")
        
        # st.markdown(f'''
        # <div class="section" style="margin-top: -1.5rem;">
        #     <div class="timeline">
        #         {timeline_html}
        #     </div>
        # </div>
        # ''', unsafe_allow_html=True)
        
        # 교육 섹션
        st.markdown('<div class="section"><h2>교육</h2></div>', unsafe_allow_html=True)
        
        # 타임라인 아이템 사용
        education_html = ""
        education_html += timeline_item("2022-24", "고려대학교 세종캠퍼스", "미디어 문예창작 전공")
        education_html += timeline_item("2024", "KGITBANK", "공공데이터 기반 데이터 분석 및 추천 시스템 챗봇 구현")
        
        st.markdown(f'''
        <div class="section" style="margin-top: -1.5rem;">
            <div class="timeline">
                {education_html}
        ''', unsafe_allow_html=True)
        st.markdown('<div class="section"><h2>취득사항</h2></div>', unsafe_allow_html=True)
        
        # 타임라인 아이템 사용 - 연도 삭제
        certifications_html = ""
        certifications_html += timeline_item("2024", "ADSP", "한국데이터산업진흥원")
        certifications_html += timeline_item("2024", "TOEIC", "865점")
        certifications_html += timeline_item("2024", "Opic", "영어 IH")
        certifications_html += timeline_item("2025", "정보처리기사", "한국산업인력공단")
        st.markdown(f'''
        <div class="section" style="margin-top: -1.5rem;">
            <div class="timeline">
                {certifications_html}
        ''', unsafe_allow_html=True)
        
    # col3에 블로그 포스팅 섹션 추가
    with col3:
        # 블로그 카드 스타일 정의
        st.markdown("""
        <style>
            .blog-container {
                margin-top: -1.5rem;
            }
            
            .blog-card-container {
                display: flex;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                margin-bottom: 20px;
                overflow: hidden;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                min-height: 180px;
                text-decoration: none !important;
                color: inherit !important;
            }
            
            .blog-card-container:hover {
                transform: translateY(-5px);
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }
            
            .blog-image-container {
                width: 35%;
                position: relative;
                overflow: hidden;
            }
            
            .blog-image-container img {
                width: 100%;
                height: 100%;
                object-fit: cover;
                position: absolute;
                top: 0;
                left: 0;
            }
            
            .blog-content-container {
                width: 65%;
                padding: 15px 20px;
                display: flex;
                flex-direction: column;
            }
            
            .blog-title {
                color: #764ba2;
                font-weight: 700;
                margin-bottom: 10px;
                font-size: 19px;
                line-height: 1.4;
                display: -webkit-box;
                -webkit-line-clamp: 2;
                -webkit-box-orient: vertical;
                overflow: hidden;
                max-height: 54px;
                font-family: 'Noto Sans KR', sans-serif;
            }
            
            .blog-date {
                color: #666;
                font-size: 12px;
                margin-bottom: 12px;
            }
            
            .blog-excerpt {
                color: #333;
                font-size: 14px;
                line-height: 1.6;
                margin-bottom: 15px;
                display: -webkit-box;
                -webkit-line-clamp: 3;
                -webkit-box-orient: vertical;
                overflow: hidden;
                flex-grow: 1;
            }
            
            .blog-read-more {
                align-self: flex-end;
                background-color: #764ba2;
                color: white;
                border: none;
                padding: 6px 12px;
                border-radius: 5px;
                font-size: 14px;
                transition: background-color 0.3s;
                display: inline-block;
                margin-top: auto;
            }
            
            .blog-read-more:hover {
                background-color: #5d3b81;
                text-decoration: none;
                color: white;
            }
        </style>
        """, unsafe_allow_html=True)
        
        # Velog.io 블로그 포스트 가져오기
        def get_velog_post_info(url):
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    # 제목 가져오기 - 제공된 XPath 사용
                    title = None
                    
                    # XPath로 제목 찾기
                    try:
                        # HTML 문서를 파싱하여 XPath 쿼리 실행
                        html_content = lxml.html.fromstring(response.text)
                        xpath_title_elements = html_content.xpath('//*[@id="root"]/div[2]/div[3]/div/h1')
                        
                        if xpath_title_elements and len(xpath_title_elements) > 0:
                            title = xpath_title_elements[0].text_content().strip()
                    except Exception as xpath_error:
                        st.warning(f"XPath 쿼리 실패: {xpath_error}")
                    
                    # XPath로 제목을 찾지 못한 경우, 기존 방식으로 시도
                    if not title:
                        # velog의 일반적인 제목 패턴 시도
                        for h1 in soup.find_all('h1'):
                            if h1.get('class') and any('sc-' in c for c in h1.get('class')):
                                title = h1.text.strip()
                                break
                    
                    # 위 두 방법으로도 찾지 못한 경우, URL에서 추출
                    if not title:
                        # URL에서 마지막 경로 부분을 가져와 타이틀로 사용
                        path_parts = url.rstrip('/').split('/')
                        last_part = path_parts[-1]
                        # 하이픈이나 언더스코어를 공백으로 변환하고 첫 글자 대문자로
                        title = ' '.join(word.capitalize() for word in re.sub(r'[-_]', ' ', last_part).split())
                    
                    # 날짜 가져오기 - velog 특화 처리
                    date = None
                    # velog의 날짜 패턴 (YYYY년 MM월 DD일) 찾기
                    for span in soup.find_all('span'):
                        if span.text and re.search(r'\d{4}년 \d{1,2}월 \d{1,2}일', span.text):
                            date = span.text.strip()
                            break
                    
                    if not date:
                        date = " "
                    
                    # 썸네일 이미지 가져오기
                    image_url = None
                    
                    # 1. Open Graph 이미지 메타 태그에서 찾기 (가장 신뢰할 수 있는 방법)
                    og_image = soup.find('meta', property='og:image') or soup.find('meta', attrs={'name': 'og:image'})
                    if og_image and og_image.get('content'):
                        image_url = og_image.get('content')
                    
                    # 2. 첫 번째 이미지 시도 (더 큰 이미지 우선)
                    if not image_url:
                        images = soup.find_all('img')
                        if images:
                            for img in images:
                                # 작은 아이콘 이미지 건너뛰기
                                if img.get('width') and int(img.get('width')) < 100:
                                    continue
                                if img.get('src') and not img.get('src').startswith('data:'):
                                    image_url = img.get('src')
                                    break
                    
                    # 3. 기본 이미지 사용
                    if not image_url:
                        # 마지막 URL 부분으로 이미지 찾기 (pip_lakeel, llamadownload 등)
                        topic = url.split('/')[-1]
                        # 주제에 따라 적절한 기본 이미지 선택
                        if 'pip' in topic.lower():
                            image_url = "https://i.imgur.com/Y1dJcQM.png"  # Python 패키지 관련 이미지
                        elif 'llama' in topic.lower():
                            image_url = "https://i.imgur.com/QgHvR8v.png"  # LLM 관련 이미지
                        else:
                            image_url = "https://i.imgur.com/JYpQCIy.jpg"  # 기본 이미지
                    
                    # 상대 URL을 절대 URL로 변환
                    if image_url and not image_url.startswith(('http://', 'https://')):
                        base_url = '/'.join(url.split('/')[:3])  # https://velog.io
                        image_url = base_url + image_url if image_url.startswith('/') else base_url + '/' + image_url
                    
                    # 요약 텍스트 가져오기
                    excerpt = None
                    
                    # 1. Open Graph 설명 메타 태그에서 찾기
                    meta_desc = soup.find('meta', property='og:description') or soup.find('meta', attrs={'name': 'description'})
                    if meta_desc and meta_desc.get('content'):
                        excerpt = meta_desc.get('content')
                    
                    # 2. 본문 첫 부분에서 가져오기
                    if not excerpt:
                        # velog 본문 div 찾기 (길이가 긴 텍스트 블록)
                        for div in soup.find_all('div'):
                            if div.text and len(div.text.strip()) > 100:
                                excerpt = div.text.strip()
                                # 200자로 제한
                                excerpt = excerpt[:200] + "..." if len(excerpt) > 200 else excerpt
                                break
                    
                    # 3. 기본 텍스트 사용
                    if not excerpt:
                        excerpt = f"{title} 블로그 포스트입니다. 클릭하여 전체 내용을 확인해보세요."
                    
                    # HTML 태그 제거하고 plaintext만 추출
                    excerpt = re.sub(r'<[^>]+>', '', excerpt)
                    
                    return {
                        "title": title,
                        "date": date,
                        "image": image_url,
                        "excerpt": excerpt,
                        "url": url
                    }
                else:
                    st.warning(f"URL에 접근할 수 없습니다: {url} (상태 코드: {response.status_code})")
                    return None
            except Exception as e:
                st.error(f"블로그 포스트 정보를 가져오는 중 오류 발생: {str(e)}")
                return {
                    "title": url.split('/')[-1].replace('-', ' ').title(),
                    "date": "날짜 정보 없음",
                    "image": "https://i.imgur.com/JYpQCIy.jpg",
                    "excerpt": "이 포스트의 내용을 불러올 수 없습니다. 클릭하여 원본 사이트에서 확인하세요.",
                    "url": url
                }
        
        # 블로그 포스트 URL 목록 - 최신 포스트가 맨 위에 오도록 정렬 (딕셔너리 형식으로 변경)
        velog_posts = {
            "Perfect prompt builder(GPTs)" : "https://velog.io/@bunhine0452/Perfect-prompt-builder-%EC%99%84%EB%B2%BD%ED%95%9C-%ED%94%84%EB%A1%AC%ED%8F%AC%ED%8A%B8-%EC%83%9D%EC%84%B1%EA%B8%B0-GPTs",
            "LLM 파인튜닝 및 양자화 편의성 툴킷" : "https://velog.io/@bunhine0452/3.-%ED%97%88%EA%B9%85%ED%8E%98%EC%9D%B4%EC%8A%A4-%EB%AA%A8%EB%8D%B8-to-.gguf-%EC%9E%90%EB%8F%99%EB%B3%80%ED%99%98-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%9E%90%EB%8F%99-%EC%A0%84%EC%B2%98%EB%A6%AC-%ED%8C%8C%EC%9D%B8%ED%8A%9C%EB%8B%9D-%ED%88%B4GUI",
            "Llama 3.2 사용하는 법 탐구": "https://velog.io/@bunhine0452/2.-Llama3.2-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94%EB%B2%95-%ED%83%90%EA%B5%AC",
            "Llama 모델 다운로드 방법": "https://velog.io/@bunhine0452/1.llamadownload",
            "pip_lakeel 패키지 개발 과정": "https://velog.io/@bunhine0452/piplakeel",
        }
        
        # 캐싱을 통해 포스트 정보 가져오기
        @st.cache_data(ttl=3600)  # 1시간 캐싱
        def fetch_all_posts_v1(posts_dict):
            posts = []
            for i, (custom_title, url) in enumerate(posts_dict.items()):
                post = get_velog_post_info(url)
                if post:
                    # velog에서 가져온 제목 대신 사용자 지정 제목 사용
                    post["title"] = custom_title
                    post["id"] = i+1
                    posts.append(post)
            return posts
        
        # 모든 포스트 정보 가져오기
        with st.spinner("블로그 포스트를 가져오는 중..."):
            blog_posts = fetch_all_posts_v1(velog_posts)
        
        # 블로그 섹션 헤더 개선
        col1_header, col2_header = st.columns([3, 1])
        
        with col1_header:
            st.markdown("""
            <h2 style="margin: 0; color: #764ba2;">최근 블로그 포스팅</h2>
            """, unsafe_allow_html=True)
        
        with col2_header:
            st.markdown("""
            <div style="text-align: right;">
                <a href="https://velog.io/@bunhine0452" target="_blank" style="text-decoration: none; color: #764ba2; font-size: 14px;">
                    전체 포스트 보기 →
                </a>
            </div>
            """, unsafe_allow_html=True)
            
            # # 개발 중에만 사용: 캐시 클리어 버튼
            # if st.button("캐시 새로고침", key="clear_cache", help="블로그 포스트 정보를 다시 로드합니다"):
            #     # 특정 함수의 캐시만 클리어
            #     fetch_all_posts_v1.clear()
            #     st.experimental_rerun()
        
        # 페이지네이션 파라미터
        POSTS_PER_PAGE = 3
        
        # 현재 페이지 가져오기 (쿼리 파라미터 또는 세션 상태)
        if 'blog_page' not in st.session_state:
            st.session_state.blog_page = 1
            
        # 페이지 변경 함수
        def change_page(page):
            st.session_state.blog_page = page
            st.experimental_rerun()
            
        # 현재 페이지에 표시할 포스트
        current_page = st.session_state.blog_page
        start_idx = (current_page - 1) * POSTS_PER_PAGE
        end_idx = start_idx + POSTS_PER_PAGE
        current_posts = blog_posts[start_idx:min(end_idx, len(blog_posts))]
        
        # 블로그 포스트 카드 렌더링
        if not blog_posts:
            st.warning("블로그 포스트를 불러오지 못했습니다.")
        else:
            for post in current_posts:
                with st.container():
                    # HTML로 카드 구성
                    html = f"""
                    <a href="{post['url']}" target="_blank" class="blog-card-container">
                        <div class="blog-image-container">
                            <img src="{post['image']}" alt="{post['title']}">
                        </div>
                        <div class="blog-content-container">
                            <div class="blog-title">{post['title']}</div>
                            <div class="blog-date">{post['date']}</div>
                            <div class="blog-excerpt">{post['excerpt']}</div>
                            <span class="blog-read-more">더 읽기 →</span>
                        </div>
                    </a>
                    """
                    st.markdown(html, unsafe_allow_html=True)
        
        # 페이지네이션 버튼 (포스트가 3개 이상일 때만 표시)
        if len(blog_posts) > POSTS_PER_PAGE:
            total_pages = (len(blog_posts) + POSTS_PER_PAGE - 1) // POSTS_PER_PAGE
            
            col1_pag, col2_pag, col3_pag = st.columns([1, 3, 1])
            
            with col1_pag:
                if current_page > 1:
                    if st.button("◀ 이전", key="prev_page"):
                        change_page(current_page - 1)
            
            with col2_pag:
                st.markdown(f"""
                <div style="text-align: center; margin-top: 10px; color: #666;">
                    {current_page} / {total_pages} 페이지
                </div>
                """, unsafe_allow_html=True)
                
            with col3_pag:
                if current_page < total_pages:
                    if st.button("다음 ▶", key="next_page"):
                        change_page(current_page + 1)
    
    # 프로젝트 섹션 (3분할 아래에 전체 너비로 배치)
    st.markdown('<div class="section"><h2 style="text-align: center;">프로젝트</h2></div>', unsafe_allow_html=True)
    
    # 프로젝트 카드를 3열 그리드로 표시하기 위한 CSS
    st.markdown("""
    <style>
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }
        
        /* 태블릿 화면에서는 2열로 표시 */
        @media (max-width: 992px) {
            .projects-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        
        /* 모바일 화면에서는 1열로 표시 */
        @media (max-width: 768px) {
            .projects-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
    """, unsafe_allow_html=True)
    
    # 카드 컴포넌트 사용
    projects_html = ""
    
    projects_html += card(
        "국민건강영양조사 기반 고혈압 예측모델",
        """<p>국민건강영양조사 데이터를 활용하여 고혈압을 예측하는 머신러닝 모델 개발. 다양한 건강 지표와 생활습관 데이터를 분석하여 고혈압 위험도를 평가하는 알고리즘 구현. 정확도와 해석 가능성을 고려하여 최적의 모델 선정.</p>
        <p><strong>기술:</strong> Python, scikit-learn, pandas, matplotlib, seaborn, 통계분석</p>""",
        f"data:image/png;base64,{get_base64_of_image('img/github_hp.png')}",
        [{"text": "GitHub 보기", "url": "https://github.com/bunhine0452/pressureproject"}]
    )
    
    projects_html += card(
        "이미지 색상화 및 손실 부분 복원 AI",
        """<p>Dacon 대회 참가 프로젝트로, 흑백 이미지를 자연스럽게 색상화하고 손상된 이미지 영역을 복원하는 딥러닝 모델 개발. GAN과 U-Net 아키텍처를 활용한 이미지 처리 파이프라인 구축. 이미지 복원에 특화된 손실 함수 설계.</p>
        <p><strong>기술:</strong> Python, PyTorch, OpenCV, TensorFlow, 컴퓨터 비전, 생성 모델</p>""",
        f"data:image/png;base64,{get_base64_of_image('img/github_base.png')}",
        [{"text": "GitHub 보기", "url": "https://github.com/bunhine0452/dacon236420"}]
    )
    
    projects_html += card(
        "AI 속성기반 감정분석 시스템",
        """<p>텍스트 데이터에서 감정을 분석하고 속성별로 분류하는 자연어 처리 모델 개발. Streamlit을 활용한 웹 인터페이스 구현으로 사용자 친화적인 분석 도구 제공. 다차원 감정 분석 및 시각화 기능 탑재.</p>
        <p><strong>기술:</strong> Python, Streamlit, BERT, Transformer, 감정분석, 자연어처리</p>""",
        f"data:image/png;base64,{get_base64_of_image('img/github_absc.png')}",
        [{"text": "GitHub 보기", "url": "https://github.com/bunhine0452/beachcombers2"}]
    )
    
    projects_html += card(
        "스타벅스 메뉴 추천 시스템",
        """<p>사용자 취향과 선호도를 분석하여 스타벅스 메뉴를 추천하는 개인화된 추천 시스템 개발. 협업 필터링과 콘텐츠 기반 필터링을 결합한 하이브리드 추천 알고리즘 구현. 사용자 프로필 기반 메뉴 선호도 예측.</p>
        <p><strong>기술:</strong> Python, Jupyter Notebook, 추천 시스템, 데이터 시각화, 머신러닝</p>""",
        f"data:image/png;base64,{get_base64_of_image('img/github_base.png')}",
        [{"text": "GitHub 보기", "url": "https://github.com/bunhine0452/Starbucks_recommend"}]
    )
    
    projects_html += card(
        "Llama GGUF 모델 실행 도구",
        """<p>대규모 언어 모델인 Llama의 GGUF 포맷 모델을 효율적으로 실행하고 활용할 수 있는 도구 개발. 로컬 환경에서 LLM을 최적화하여 구동하는 방법 연구. 메모리 사용량 최적화 및 추론 속도 개선.</p>
        <p><strong>기술:</strong> Python, Jupyter Notebook, LLM, GGUF, llama.cpp, 최적화</p>""",
        f"data:image/png;base64,{get_base64_of_image('img/github_base.png')}",
        [{"text": "GitHub 보기", "url": "https://github.com/bunhine0452/run_llama_gguf"}]
    )
    
    projects_html += card(
        "pip_lakeel 패키지 도구",
        """<p>Python 패키지 관리 및 배포를 위한 전문 도구 개발. 표준화된 패키지 구조와 배포 프로세스를 자동화하여 개발 효율성 향상. 의존성 관리 및 버전 제어 기능 통합.</p>
        <p><strong>기술:</strong> Python, pip, 패키지 관리, 자동화, CI/CD</p>""",
        f"data:image/png;base64,{get_base64_of_image('img/github_base.png')}",
        [{"text": "GitHub 보기", "url": "https://github.com/bunhine0452/pip_lakeel"}]
    )
    
    # HTML div 태그가 직접 화면에 보이는 문제 수정
    st.markdown(f'''
    <div class="section" style="margin-top: -1.5rem;">
        <div class="projects-grid">
            {projects_html}
        
    </div>
    ''', unsafe_allow_html=True)
    
    # 푸터
    st.markdown("""
    <div style="text-align: center; margin-top: 2rem; color: #666;">
        © 2025 KimHyunbin. All Rights Reserved.
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()


