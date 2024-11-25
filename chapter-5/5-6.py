import streamlit as st
# 添加文本输入框
name = st.text_input(' 请输入您的姓名：')
# 添加数字输入框
age = st.number_input(' 请输入您的年龄：', min_value=0, max_value=150, step=1)
# 添加下拉菜单
gender = st.selectbox(' 请选择您的性别：', ['Male', 'Female'])
# 添加滑动条
income = st.slider(' 请选择您的年收入：', min_value=0, max_value=100000, step=1000)
# 打印用户输入的信息
st.write(f' 您的姓名是：{name}')
st.write(f' 您的年龄是：{age}')
st.write(f' 您的性别是：{gender}')
st.write(f' 您的年收入是：{income}')