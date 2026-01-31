import streamlit as st
import time

# --- 1. 页面基础配置 ---
st.set_page_config(
    page_title="凯文老师的✨成绩魔法屋✨",
    page_icon="🐰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. 暴力适配 CSS (修复按钮缩成一团的问题) ---
st.markdown("""
    <style>
    /* 强制背景渐变：还原 HTML 效果 */
    .stApp {
        background-image: linear-gradient(120deg, #fccb90 0%, #d57eeb 100%) !important;
        background-attachment: fixed !important;
    }

    /* 隐藏 Streamlit 默认的页眉、页脚和红条 */
    header, footer, .viewerBadge_container__1QSob {
        visibility: hidden !important;
        display: none !important;
    }

    /* 中间白色卡片适配 */
    .block-container {
        background: rgba(255, 255, 255, 0.95) !important;
        border-radius: 30px !important;
        padding: 2.5rem 1.5rem !important;
        margin-top: 40px !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1) !important;
        max-width: 400px !important;
    }

    /* 手机端宽度修正 */
    @media only screen and (max-width: 600px) {
        .block-container {
            width: 90% !important;
            margin-top: 20px !important;
        }
    }

    /* 标题样式 */
    h1 {
        color: #ff8e9e !important;
        text-align: center !important;
        font-weight: 800 !important;
        font-size: 24px !important;
    }

    /* 输入框药丸形状适配 */
    div[data-testid="stTextInput"] input {
        border-radius: 50px !important;
        border: 2px solid #ffcccc !important;
        height: 55px !important;
        text-align: center !important;
        font-size: 18px !important;
    }

    /* 核心修复：强制按钮撑满全宽，解决缩在左边的问题 */
    .stButton, div.stButton {
        width: 100% !important;
        display: flex !important;
        justify-content: center !important;
    }
    
    div.stButton > button {
        width: 100% !important; /* 关键：强制 100% 宽度 */
        background: linear-gradient(to right, #ff9a9e 0%, #fecfef 100%) !important;
        color: white !important;
        border-radius: 50px !important;
        height: 55px !important;
        border: none !important;
        font-size: 18px !important;
        font-weight: bold !important;
        box-shadow: 0 5px 15px rgba(255, 154, 158, 0.4) !important;
    }

    /* 结果显示框 */
    .result-card {
        background: #FFF0F5;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        border: 2px dashed #ffb7c5;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. 模拟数据 ---
student_database = {
    "13800138000": {"name": "小樱 🌸", "scores": "语文: 98 | 数学: 95 | 魔法: SS"},
    "123456": {"name": "测试宝宝 👶", "scores": "吃饭: 100 | 睡觉: 100"}
}

# --- 4. 界面展示 ---
st.markdown("<h1>🐰 期末成绩查询</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#a4b0be; font-size:14px; margin-bottom:25px;'>请输入手机号召唤成绩单</p>", unsafe_allow_html=True)

# 隐藏 Label 的输入框
phone_input = st.text_input("label", placeholder="在此输入手机号...", label_visibility="collapsed")

if st.button("✨ 查询 ✨"):
    if not phone_input:
        st.warning("⚠️ 还没输入手机号哦")
    elif phone_input in student_database:
        with st.spinner('🐰 正在查找...'):
            time.sleep(0.5)
        data = student_database[phone_input]
        st.markdown(f"""
            <div class="result-card">
                <h3 style="color:#ff6b81; margin:0;">🎉 找到啦: {data['name']}</h3>
                <p style="margin-top:10px;">{data['scores']}</p>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("🚫 没找到这个号码")

st.markdown("<div style='text-align: center; color: #fff; margin-top: 50px; opacity: 0.6; font-size: 12px;'>☁️ 凯文老师的成绩魔法屋</div>", unsafe_allow_html=True)
