import streamlit as st
# 创建两列布局
col1, col2 = st.columns(2)
# 在第一列添加文本内容
with col1:
    st.header(' 左侧列 ')
    st.text(' 这是第一列的文本内容。')

# 在第二列添加图表
with col2:
    st.header(' 右侧列 ')
    st.bar_chart({'A': 10, 'B': 20, 'C': 30})