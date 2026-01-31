import streamlit as st
import time

# --- 1. 手机端专属配置 ---
st.set_page_config(
    page_title="凯文老师的成绩魔法屋",
    page_icon="🐰",
    layout="wide",  # 关键：手机上要用 wide 模式，不要 centered
    initial_sidebar_state="collapsed"
)

# --- 2. 手机端核心 CSS (APP 风格) ---
st.markdown("""
    <style>
    /* 全局重置：强制浅色模式，防止手机夜间模式破坏配色 */
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(135deg, #fccb90 10%, #d57eeb 100%);
        background-attachment: fixed;
    }
    
    /* 强制隐藏 Streamlit 自带的顶部红条和菜单 */
    header, footer, [data-testid="stHeader"] {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
    }

    /* === 卡片容器：手机上做成浮层效果 === */
    .block-container {
        padding: 2rem 1rem !important; /* 上下留空，左右窄边 */
        max-width: 100% !important;
    }
    
    .mobile-card {
        background: rgba(255, 255, 255, 0.96);
        border-radius: 25px;
        padding: 30px 20px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        margin-top: 10vh; /* 距离顶部 10% 高度，视觉重心更稳 */
    }

    /* === 标题优化 === */
    h1 {
        color: #ff7e95 !important;
        font-size: 26px !important;
        text-align: center;
        font-weight: 800 !important;
        margin-bottom: 5px !important;
        padding: 0 !important;
    }
    p {
        color: #aab0c0 !important;
        text-align: center;
        font-size: 14px;
    }

    /* === 输入框：超大圆角 === */
    div[data-testid="stTextInput"] input {
        background-color: #f8f9fa !important;
        border: 2px solid #ffe0e6 !important;
        border-radius: 50px !important;
        height: 60px !important; /* 加高 */
        font-size: 18px !important;
        text-align: center;
        color: #333 !important;
        box-shadow: none !important;
        -webkit-appearance: none; /* 修复 iOS 阴影 */
    }
    div[data-testid="stTextInput"] input:focus {
        border-color: #ff6b81 !important;
        background-color: #fff !important;
    }

    /* === 按钮：全宽 + 渐变 === */
    .stButton {
        width: 100% !important;
        padding-top: 10px !important;
    }
    div.stButton > button {
        width: 100% !important; /* 强制占满宽度 */
        background: linear-gradient(90deg, #ff9a9e 0%, #fecfef 100%) !important;
        border: none !important;
        border-radius: 50px !important;
        height: 60px !important; /* 加高 */
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        box-shadow: 0 10px 20px rgba(255, 154, 158, 0.3) !important;
    }
    div.stButton > button:active {
        transform: scale(0.98);
        box-shadow: 0 5px 10px rgba(255, 154, 158, 0.3) !important;
    }

    /* === 结果弹窗 === */
    .result-box {
        background: #fff0f5;
        border-radius: 20px;
        padding: 20px;
        margin-top: 25px;
        text-align: center;
        border: 2px dashed #ffc3d0;
        animation: fadeIn 0.5s ease;
    }
    @keyframes fadeIn {from {opacity:0; transform:translateY(10px);} to {opacity:1;}}
    </style>
""", unsafe_allow_html=True)

# --- 3. 数据 ---
student_database = {
    "13800138000": {"name": "小樱 🌸", "scores": "语文: 98 | 数学: 95 | 魔法: SS"},
    "13911112222": {"name": "鸣人 🍥", "scores": "忍术: 60 | 影分身: 100"},
    "123456": {"name": "测试宝宝 👶", "scores": "吃饭: 100 | 睡觉: 100"}
}

# --- 4. 界面逻辑 (使用 HTML 容器包裹，模拟 APP 结构) ---
st.markdown('<div class="mobile-card">', unsafe_allow_html=True)

st.markdown("<h1>🐰 凯文老师的<br>✨成绩魔法屋✨</h1>", unsafe_allow_html=True)
st.markdown("<p>请输入预留手机号查询</p>", unsafe_allow_html=True)

# 输入区
phone_input = st.text_input("label", placeholder="在此输入手机号...", label_visibility="collapsed")

# 按钮区
if st.button("🚀 立即查询"):
    if not phone_input:
        st.warning("⚠️ 请先输入手机号")
    elif phone_input in student_database:
        with st.spinner("🐰 正在翻阅成绩单..."):
            time.sleep(0.6)
        
        data = student_database[phone_input]
        
        # 结果展示
        st.markdown(f"""
            <div class="result-box">
                <h3 style="color:#ff6b81; margin:0 0 10px 0;">🎉 找到学员：{data['name']}</h3>
                <div style="color:#555; font-size:16px; line-height:1.8;">
                    {data['scores']}
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("🚫 未找到该号码，请核对")

st.markdown('</div>', unsafe_allow_html=True)

# 底部版权 (淡色)
st.markdown("<div style='text-align:center; margin-top:30px; color:rgba(255,255,255,0.7); font-size:12px;'>☁️ 凯文老师专属查询系统</div>", unsafe_allow_html=True)
