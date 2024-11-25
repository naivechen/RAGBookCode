# app.py
import streamlit as st
import pandas as pd 
import numpy as np 
def main():
    st.title(' 交互式数据可视化应用程序 ')
    # 添加文本
    st.write(' 欢迎使用 Streamlit 构建交互式 Web 应用程序！ ')

    # 添加数据表格
    st.write(' 下面是一个简单的数据表格：')
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
    df = pd.DataFrame(data)
    st.write(df)

    # 添加图表
    st.write(' 下面是一个简单的折线图：')
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
        )
    st.line_chart(chart_data)

    # 添加输入组件
    st.write(' 请在下方输入框中输入您的姓名：')
    name = st.text_input(' 姓名 ', 'John Doe')
    st.write(f' 您输入的姓名是：{name}')

    # 添加按钮
    if st.button(' 点击这里 '):
        st.write(' 您点击了按钮！ ')

    # 添加复选框
    option = st.checkbox(' 显示 / 隐藏文本 ')
    if option:
        st.write(' 这是一个隐藏的文本。')

    # 添加下拉菜单
    option = st.selectbox(
        ' 请选择一个选项：',
        [' 选项 1', ' 选项 2', ' 选项 3']
        )
    st.write(f' 您选择了：{option}')

if __name__ == '__main__':
    main()