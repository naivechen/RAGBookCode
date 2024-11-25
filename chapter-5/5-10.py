import streamlit as st
import time
# 添加进度条
progress_bar = st.progress(0)
# 模拟数据加载过程
for i in range(100):
    time.sleep(0.1)
    progress_bar.progress(i + 1)

# 添加加载动画
with st.spinner(' 正在加载，请稍候 ...'):
    time.sleep(5)
    st.success(' 加载完成 !')