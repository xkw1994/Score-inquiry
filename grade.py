import streamlit as st
import time

# --- 1. 页面配置 ---
st.set_page_config(
    page_title="凯文老师的✨成绩魔法屋✨",
    page_icon="🐰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. 暴力 CSS (只做居中这一件事) ---
st.markdown("""
    <style>
    /* 全局背景 */
    .stApp {
        background-image: linear-gradient(120deg, #fccb90 0%, #d57eeb 100%) !important;
        background-attachment: fixed !important;
        font-family: "Microsoft YaHei", sans-serif !important;
    }
    
    /* 隐藏杂项 */
    header, footer, .viewerBadge_container__1QSob { display: none !important; }

    /* 卡片容器：手机端适配 */
    .block-container {
        background: rgba(255, 255, 255, 0.95) !important;
        border-radius: 30px !important;
        padding: 3rem 1rem !important; /* 上下宽一点，左右窄一点 */
        margin-top: 40px !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15) !important;
        max-width: 420px !important;
    }
    @media only screen and (max-width: 600px) {
        .block-container {
            width: 90% !important;
            margin-top: 20px !important;
        }
    }

    /* 标题 */
    h1 {
        color: #ff8e9e !important;
        text-align: center !important;
        font-size: 26px !important;
        font-weight: 800 !important;
        margin-bottom: 20px !important;
    }

    /* === ⚡️ 核心修复：输入框居中 + 高度 === */
    /* 1. 锁定输入框外层容器的宽度，并居中 */
    div[data-testid="stTextInput"] {
        width: 85% !important;        /* 宽度只占 85% */
        margin-left: auto !important; /* 左边自动 */
        margin-right: auto !important;/* 右边自动 -> 结果就是居中 */
    }

    /* 2. 修改输入框本体样式 */
    div[data-baseweb="input"] {
        border-radius: 50px !important;
        border: 2px solid #ffcccc !important;
        background-color: #fff !important;
        height: 60px !important;      /* 强制高度 60px */
        padding: 0 15px !important;
    }
    div[data-baseweb="input"] input {
        text-align: center !important;
        font-size: 18px !important;
        color: #555 !important;
    }

    /* === ⚡️ 核心修复：按钮居中 === */
    /* 1. 锁定按钮外层容器的宽度，并居中 */
    .stButton {
        width: 85% !important;        /* 跟输入框一样宽 */
        margin-left: auto !important; /* 强制居中 */
        margin-right: auto !important;/* 强制居中 */
        margin-top: 20px !important;
        display: block !important;    /* 块级元素才能居中 */
    }

    /* 2. 按钮本体填满容器 */
    div.stButton > button {
        width: 100% !important;       /* 填满那 85% 的宽度 */
        height: 60px !important;
        background: linear-gradient(to right, #ff9a9e 0%, #fecfef 100%) !important;
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        font-size: 20px !important;
        font-weight: bold !important;
        box-shadow: 0 8px 20px rgba(255, 154, 158, 0.4) !important;
    }
    div.stButton > button:active {
        transform: scale(0.98);
    }
    
    /* 结果卡片 */
    .result-card {
        background: #FFF0F5;
        border: 2px dashed #ffb7c5;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        margin-top: 30px;
        width: 90% !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. 数据 ---
student_database = {
    "13800138000": {"name": "小樱 🌸", "scores": "语文: 98 | 数学: 95 | 魔法: SS"},
    "123456": {"name": "测试宝宝 👶", "scores": "吃饭: 100 | 睡觉: 100"}
}

# --- 4. 界面逻辑 ---
st.markdown("<h1>🐰 期末成绩查询</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#ccc; font-size:14px; margin-bottom:10px;'>请输入手机号召唤成绩单</p>", unsafe_allow_html=True)

phone_input = st.text_input("label", placeholder="在此输入手机号...", label_visibility="collapsed")

if st.button("✨ 查 询 ✨"):
    if not phone_input:
        st.warning("⚠️ 还没输入手机号哦")
    elif phone_input in student_database:
        with st.spinner('🐰 正在查找...'):
            time.sleep(0.5)
        data = student_database[phone_input]
        st.markdown(f"""
            <div class="result-card">
                <h3 style="color:#ff6b81; margin:0 0 10px 0;">🎉 找到啦: {data['name']}</h3>
                <div style="font-size:16px; line-height:1.8; color:#555;">{data['scores']}</div>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("🚫 没找到这个号码")

st.markdown("<div style='text-align: center; color: #fff; margin-top: 50px; opacity: 0.6; font-size: 12px;'>☁️ 凯文老师的成绩魔法屋</div>", unsafe_allow_html=True)
