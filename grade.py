import streamlit as st
import time

# 1. 页面基础设置
st.set_page_config(page_title="✨ 魔法成绩屋 ✨", page_icon="🐰", layout="centered")

# 2. 🎨 CSS 魔法样式 (让 Python 界面变可爱的关键)
# 这段代码把 Streamlit 默认的丑丑界面改成了粉色渐变风格
st.markdown("""
    <style>
    /* 全局背景：粉紫渐变 */
    .stApp {
        background-image: linear-gradient(120deg, #fccb90 0%, #d57eeb 100%);
        font-family: "Microsoft YaHei", sans-serif;
    }
    
    /* 模拟那个白色的“卡片”容器 */
    .main .block-container {
        background: rgba(255, 255, 255, 0.95);
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        max-width: 500px; /* 限制宽度，看起来像手机 */
        margin-top: 50px;
    }

    /* 标题样式 */
    h1 {
        color: #ff6b81 !important;
        text-align: center;
        font-weight: bold;
        font-size: 2rem;
        padding-bottom: 10px;
    }
    
    /* 输入框样式 */
    div[data-testid="stTextInput"] input {
        border-radius: 50px;
        border: 2px solid #ffcccc;
        text-align: center;
        height: 50px;
        font-size: 18px;
        color: #555;
    }
    
    /* 输入框聚焦时的效果 */
    div[data-testid="stTextInput"] input:focus {
        border-color: #ff6b81;
        box-shadow: 0 0 8px rgba(255, 107, 129, 0.3);
    }

    /* 按钮样式：粉色渐变 */
    div.stButton > button {
        background: linear-gradient(to right, #ff9a9e 0%, #fecfef 100%);
        color: white;
        border-radius: 50px;
        height: 50px;
        width: 100%;
        border: none;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 5px 15px rgba(255, 154, 158, 0.4);
        transition: 0.3s;
    }
    
    /* 按钮悬停效果 */
    div.stButton > button:hover {
        transform: scale(1.02);
        color: white;
        border: none;
    }

    /* 隐藏右上角菜单和底部 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    </style>
""", unsafe_allow_html=True)

# 3. 💾 数据中心 (以后可以换成读取 Excel)
student_database = {
    "13800138000": {"name": "小樱 🌸", "scores": "语文: 98 | 数学: 95 | 魔法: SS"},
    "13911112222": {"name": "鸣人 🍥", "scores": "忍术: 60 | 影分身: 100"},
    "123456": {"name": "测试宝宝 👶", "scores": "吃饭: 100 | 睡觉: 100"}
}

# 4. 🖥️ 界面布局逻辑
st.markdown("<h1>🐰 期末成绩查询</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a4b0be; margin-bottom: 30px;'>请输入手机号召唤成绩单</p>", unsafe_allow_html=True)

# 输入框
phone_input = st.text_input("input", placeholder="在此输入手机号...", label_visibility="collapsed")

# 占个空行
st.write("") 

# 按钮逻辑
if st.button("✨ 立即查询 ✨"):
    if not phone_input:
        st.warning("🐷 还没有输入手机号哦！")
    
    elif phone_input in student_database:
        # 模拟一点加载感
        with st.spinner('正在召唤数据...'):
            time.sleep(0.8)
        
        student = student_database[phone_input]
        
        # 显示结果 (使用了 Streamlit 的 info 盒子，并自定义了样式)
        st.success(f"🎉 查到了！学员: **{student['name']}**")
        st.info(f"📝 成绩详情:\n\n{student['scores']}")
        st.balloons() # 放气球特效
        
    else:
        st.error("🚫 哎呀，没有找到这个号码的记录。\n请检查一下是不是输错了？")

# 底部小字
st.markdown("<div style='text-align: center; margin-top: 50px; color: #ddd; font-size: 12px;'>☁️ Powered by Streamlit Cloud</div>", unsafe_allow_html=True)
