import streamlit as st
import pandas as pd

# --- 1. 页面配置 (网页标签和图标) ---
st.set_page_config(page_title="🌸 魔法成绩查询", page_icon="🐰")

# --- 2. 模拟数据库 (为了安全，以后可以换成读取Excel) ---
# 真实使用时，建议把这里改成读取 excel 文件: df = pd.read_excel("grades.xlsx")
data = {
    "13800138000": {"name": "小樱 🌸", "result": "语文: 98 | 数学: 95 | 魔法: SS"},
    "123456": {"name": "测试宝宝 👶", "result": "吃饭: 100 | 睡觉: 100"},
    "13911112222": {"name": "鸣人 🍥", "result": "忍术: 60 | 影分身: 100"}
}

# --- 3. 界面设计 (CSS 美化) ---
# 隐藏掉右上角的菜单，让界面更干净
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stApp {background-image: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# 标题
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🎀 期末成绩查询屋 🎀</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>👇 请输入预留的手机号召唤成绩单</p>", unsafe_allow_html=True)

# --- 4. 输入与查询逻辑 ---
phone = st.text_input("手机号", placeholder="在此输入...", max_chars=11)

if st.button("✨ 点击查询 ✨", type="primary"):
    if not phone:
        st.warning("⚠️ 请先输入手机号哦！")
    elif phone in data:
        # 查到了！放个气球庆祝一下
        st.balloons()
        student = data[phone]
        
        # 使用卡片展示结果
        st.success(f"🎉 找到啦！学员：{student['name']}")
        st.info(f"📝 成绩详情：\n\n{student['result']}")
    else:
        st.error("🚫 哎呀，没有找到这个号码的记录。\n请检查是否输错，或联系老师确认。")

# 底部版权
st.markdown("---")
st.markdown("<div style='text-align: center; font-size: 12px; color: #aaa;'>☁️ Powered by 爱心魔法屋</div>", unsafe_allow_html=True)