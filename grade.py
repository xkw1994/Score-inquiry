import streamlit as st
import time

# --- 1. 页面基础配置 ---
st.set_page_config(
    page_title="凯文老师的✨成绩魔法屋✨",
    page_icon="🐰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. 针对手机截图问题的暴力修复 CSS ---
st.markdown("""
    <style>
    /* 1. 全局字体与背景 */
    .stApp {
        background-image: linear-gradient(120deg, #fccb90 0%, #d57eeb 100%);
        background-attachment: fixed;
        font-family: "Microsoft YaHei", sans-serif !important;
    }

    /* 2. 中间卡片：修复内边距 */
    .block-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 30px;
        padding: 2rem !important;
        margin-top: 40px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        max-width: 420px;
    }

    /* === 📱 手机端强制适配 (针对 IMG_3587 修复) === */
    @media only screen and (max-width: 600px) {
        .block-container {
            width: 90% !important;
            padding: 2rem 1.5rem !important;
            margin-top: 30px !important;
        }
        
        /* 强制隐藏 Streamlit 的红条 footer */
        footer, header, .viewerBadge_container__1QSob {
            visibility: hidden !important;
            display: none !important;
        }
    }

    /* 3. 标题样式 */
    h1 {
        color: #ff8e9e !important;
        text-align: center;
        font-weight: 800;
        font-size: 24px !important;
        padding: 0;
        margin-bottom: 5px;
        border: none;
    }
    
    .subtitle {
        text-align: center;
        color: #a4b0be;
        font-size: 14px;
        margin-bottom: 30px;
    }

    /* 4. 输入框：使用最高优先级 !important 修复样式 */
    div[data-testid="stTextInput"] {
        margin-top: 0px; /* 调整间距 */
    }
    
    div[data-testid="stTextInput"] input {
        border-radius: 50px !important; /* 强制圆角 */
        border: 2px solid #ffcccc !important;
        background-color: #fff !important;
        text-align: center;
        height: 55px !important; /* 强制高度 */
        font-size: 18px !important;
        color: #555 !important;
        padding: 0 20px !important;
    }
    
    /* 选中时效果 */
    div[data-testid="stTextInput"] input:focus {
        border-color: #ff6b81 !important;
        box-shadow: 0 0 10px rgba(255, 107, 129, 0.3) !important;
    }

    /* 5. 按钮：核心修复点！让它变宽 */
    
    /* 首先强制按钮的容器占满宽度 */
    .stButton {
        width: 100% !important;
        margin-top: 15px !important;
    }
    
    /* 然后强制按钮本身占满容器 */
    div.stButton > button {
        width: 100% !important;  /* 这一行修复了“按钮缩在左边”的问题 */
        background: linear-gradient(to right, #ff9a9e 0%, #fecfef 100%) !important;
        color: white !important;
        border-radius: 50px !important;
        height: 55px !important;
        border: none !important;
        font-size: 18px !important;
        font-weight: bold !important;
        box-shadow: 0 5px 15px rgba(255, 154, 158, 0.4) !important;
        display: block !important; /* 确保它是块级元素 */
    }
    
    div.stButton > button:active {
        transform: scale(0.98);
    }
    
    /* 结果框 */
    .result-card {
        background: #FFF0F5;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        color: #555;
        border: 2px dashed #ffb7c5;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. 模拟数据 ---
student_database = {
    "13800138000": {"name": "小樱 🌸", "scores": "语文: 98 | 数学: 95 | 魔法: SS"},
    "13911112222": {"name": "鸣人 🍥", "scores": "忍术: 60 | 影分身: 100"},
    "123456": {"name": "测试宝宝 👶", "scores": "吃饭: 100 | 睡觉: 100"}
}

# --- 4. 界面内容 ---

# 标题
st.markdown("<h1>🐰 期末成绩查询</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>请输入手机号召唤成绩单</p>", unsafe_allow_html=True)

# 输入框
phone_input = st.text_input("label", placeholder="在此输入手机号...", label_visibility="collapsed")

# 按钮
if st.button("✨ 查询 ✨"):
    if not phone_input:
        st.warning("⚠️ 还没输入手机号哦")
    elif phone_input in student_database:
        # 加载动画
        with st.spinner('🐰 正在查找...'):
            time.sleep(0.5)
        
        data = student_database[phone_input]
        
        # 结果展示
        st.markdown(f"""
            <div class="result-card">
                <h3 style="color:#ff6b81; margin:0 0 10px 0;">🎉 找到啦: {data['name']}</h3>
                <div style="line-height: 1.6;">{data['scores']}</div>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("🚫 没找到这个号码")

# 底部文字
st.markdown("<div style='text-align: center; color: #fff; margin-top: 40px; opacity: 0.8; font-size: 12px;'>☁️ 凯文老师的成绩魔法屋</div>", unsafe_allow_html=True)

# 强制隐藏自带的红条footer
st.markdown("""
    <style>
    .viewerBadge_container__1QSob {display: none !important;}
    footer {display: none !important;}
    </style>
""", unsafe_allow_html=True)
