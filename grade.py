import streamlit as st
import time

# --- 1. 页面基础配置 ---
st.set_page_config(
    page_title="凯文老师的✨成绩魔法屋✨",
    page_icon="🐰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. 这里的 CSS 是还原截图效果的关键 ---
st.markdown("""
    <style>
    /* 1. 背景：严格还原截图的“橙色-粉色-紫色”渐变 */
    .stApp {
        background-image: linear-gradient(120deg, #fccb90 0%, #d57eeb 100%);
        background-attachment: fixed;
        font-family: "Microsoft YaHei", sans-serif !important;
    }

    /* 2. 中间那个白色的卡片 */
    .block-container {
        background: rgba(255, 255, 255, 0.95); /* 纯白背景，微透 */
        border-radius: 30px;       /* 大圆角 */
        padding: 2.5rem 1.5rem !important;
        margin-top: 40px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1); /* 柔和阴影 */
        max-width: 400px;          /* 限制宽度，模仿手机比例 */
    }

    /* === 📱 手机端专属修正 === */
    @media only screen and (max-width: 600px) {
        .block-container {
            margin-top: 20px !important; /* 手机上不要离顶部太远 */
            width: 90% !important;       /* 宽度占屏幕90% */
            padding: 2rem 1.2rem !important;
        }
        /* 手机上隐藏顶部菜单，防止遮挡 */
        #MainMenu, header, footer {visibility: hidden;}
    }

    /* 3. 标题样式 */
    h1 {
        color: #ff8e9e !important; /* 标题也是粉粉的颜色 */
        text-align: center;
        font-weight: 800;
        font-size: 26px !important;
        padding: 0;
        margin-bottom: 5px;
        border: none;
    }
    
    /* 副标题样式 */
    .subtitle {
        text-align: center;
        color: #a4b0be;
        font-size: 14px;
        margin-bottom: 30px;
        font-weight: normal;
    }

    /* 4. 输入框：还原“药丸”形状 (Pill Shape) */
    div[data-testid="stTextInput"] input {
        border-radius: 50px !important;  /* 像胶囊一样的圆角 */
        border: 2px solid #ffcccc;
        background-color: #fff;
        text-align: center;
        height: 55px;
        font-size: 18px;
        color: #555;
        padding-left: 20px;
        padding-right: 20px;
    }
    
    /* 输入框选中时 */
    div[data-testid="stTextInput"] input:focus {
        border-color: #ff6b81;
        box-shadow: 0 0 10px rgba(255, 107, 129, 0.3);
    }

    /* 5. 按钮：还原截图里的粉色渐变 + 药丸形状 */
    div.stButton > button {
        background: linear-gradient(to right, #ff9a9e 0%, #fecfef 100%);
        color: white !important;
        border-radius: 50px !important; /* 像胶囊一样的圆角 */
        height: 55px;
        width: 100%;
        border: none;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 5px 15px rgba(255, 154, 158, 0.4);
        margin-top: 15px;
    }
    
    div.stButton > button:active {
        transform: scale(0.98);
    }
    
    /* 隐藏输入框上面的label */
    label[data-testid="stWidgetLabel"] {
        display: none;
    }
    
    /* 结果显示框 */
    .result-card {
        background: #FFF0F5;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        color: #555;
        border: 2px dashed #ffb7c5;
        margin-top: 20px;
        font-size: 16px;
    }

    </style>
""", unsafe_allow_html=True)

# --- 3. 模拟数据 ---
student_database = {
    "13800138000": {"name": "小樱 🌸", "scores": "语文: 98 | 数学: 95 | 魔法: SS"},
    "13911112222": {"name": "鸣人 🍥", "scores": "忍术: 60 | 影分身: 100"},
    "123456": {"name": "测试宝宝 👶", "scores": "吃饭: 100 | 睡觉: 100"}
}

# --- 4. 界面内容 (完全模仿截图布局) ---

# 标题区域
st.markdown("<h1>🐰 期末成绩查询</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>请输入手机号召唤成绩单</p>", unsafe_allow_html=True)

# 输入框
phone_input = st.text_input("label", placeholder="在此输入手机号...", label_visibility="collapsed")

# 按钮
if st.button("✨ 查询 ✨"):
    if not phone_input:
        st.warning("⚠️ 还没输入手机号哦")
    elif phone_input in student_database:
        # 模拟加载
        with st.spinner('🐰 正在查找...'):
            time.sleep(0.5)
        
        data = student_database[phone_input]
        
        # 结果展示
        st.markdown(f"""
            <div class="result-card">
                <h3 style="color:#ff6b81; margin:0;">🎉 找到啦: {data['name']}</h3>
                <br>
                {data['scores']}
            </div>
        """, unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("🚫 没找到这个号码")

# 底部版权
st.markdown("<div style='text-align: center; color: #fff; margin-top: 50px; opacity: 0.6; font-size: 12px;'>☁️ 凯文老师的成绩魔法屋</div>", unsafe_allow_html=True)
