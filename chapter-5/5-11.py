import streamlit as st
# 添加单选按钮
option = st.radio(' 请选择一个选项：', ['A', 'B', 'C'])
# 根据用户选择的选项执行不同的操作
if option == 'A':
 st.write(' 您选择了选项 A。')
elif option == 'B':
 st.write(' 您选择了选项 B。')
else:
 st.write(' 您选择了选项 C。')