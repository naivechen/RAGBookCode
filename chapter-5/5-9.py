import streamlit as st
# 添加聊天框
user_input = st.text_area(" 请输入您的消息：")
# 程序逻辑处理
if user_input:
    st.write(f" 用户输入的消息是：{user_input}")
    st.write(" 程序回复的消息是：您好！欢迎使用我们的应用程序。")