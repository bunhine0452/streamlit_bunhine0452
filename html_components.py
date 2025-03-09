import streamlit as st

def rounded_image(image_url, width="100%", border_radius="10px"):
    """둥근 이미지 컴포넌트"""
    return f"""
    <div style="display: flex; justify-content: center;">
        <img src="{image_url}" style="width: {width}; border-radius: {border_radius}; max-width: 100%;">
    </div>
    """

def timeline_item(year, title, description):
    """타임라인 아이템 컴포넌트"""
    return f"""
    <div style="display: flex; margin-bottom: 20px;">
        <div style="min-width: 80px; font-weight: bold; color: #764ba2;">{year}</div>
        <div style="border-left: 2px solid #764ba2; padding-left: 15px;">
            <div style="font-weight: bold; margin-bottom: 5px;">{title}</div>
            <div style="color: #444;">{description}</div>
        </div>
    </div>
    """

def social_media_icon(icon_name, url, color="white"):
    """소셜 미디어 아이콘 컴포넌트"""
    icons = {
        "github": "fab fa-github",
        "linkedin": "fab fa-linkedin",
        "twitter": "fab fa-twitter",
        "facebook": "fab fa-facebook",
        "instagram": "fab fa-instagram",
        "email": "fas fa-envelope",
        "chain" : "fas fa-link",
        "pencil" : "fa fa-pencil",
        "message" : "fas fa-message"
        
    }
    
    icon_class = icons.get(icon_name.lower(), "fas fa-link")
    
    return f"""
    <a href="{url}" target="_blank" style="text-decoration: none; color: {color}; margin: 0 10px;">
        <i class="{icon_class}" style="font-size: 24px;"></i>
    </a>
    """

def skill_progress_bar(skill_name, percentage, color="#764ba2"):
    """스킬 진행 막대 컴포넌트"""
    return f"""
    <div style="margin-bottom: 15px;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
            <span>{skill_name}</span>
            <span>{percentage}%</span>
        </div>
        <div style="height: 8px; background-color: #f0f0f0; border-radius: 4px;">
            <div style="height: 100%; width: {percentage}%; background: linear-gradient(90deg, white 0%, {color} 100%); border-radius: 4px;"></div>
        </div>
    </div>
    """

def card(title, content, image_url=None, buttons=None):
    """프로젝트 카드 컴포넌트"""
    # 이미지 HTML
    if image_url:
        image_html = f'<img src="{image_url}" alt="{title}" />'
    else:
        image_html = ""
    
    # 링크 URL (첫 번째 버튼의 URL을 사용)
    link_url = "#"
    if buttons and len(buttons) > 0:
        link_url = buttons[0]["url"]
    
    # 기술 태그 추출
    if "<strong>기술:</strong>" in content:
        # 본문과 기술 태그 분리
        main_content, tech_part = content.split("<strong>기술:</strong>")
        # 기술 태그 추출 및 포맷팅
        techs = tech_part.strip().replace("<p>", "").replace("</p>", "").split(", ")
        tech_tags_html = '<div class="tech-tags">'
        for tech in techs:
            tech_tags_html += f'<span class="tech-tag">{tech}</span>'
        tech_tags_html += '</div>'
        
        content = f"{main_content}<div style='margin: 10px 0;'>{tech_tags_html}</div>"
    
    return f"""
    <a href="{link_url}" target="_blank" class="project-card-link">
        <div class="project-card">
            {image_html}
            <h4 class="project-title">{title}</h4>
            <div class="project-content">{content}</div>
        </div>
    </a>
    """
    
def add_fontawesome():
    """Font Awesome 아이콘 추가"""
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" integrity="sha512-Fo3rlrZj/k7ujTnHg4CGR2D7kSs0v4LLanw2qksYuRlEzO+tcaEPQogQ0KaoGN26/zrn20ImR1DfuLWnOo7aBA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    """, unsafe_allow_html=True) 