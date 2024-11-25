import streamlit as st
import pandas as pd
import numpy as np 
# 加载数据
@st.cache_data
def load_data():
    # 在这里加载您的数据
    # 例如，使用 pandas.read_csv() 函数从 CSV 文件中加载数据
    data = pd.DataFrame(np.random.randn(100, 2), columns=['Feature1', 'Feature2'])
    return data

data = load_data()
# 绘制折线图
st.subheader(' 折线图示例 ')
st.line_chart(data)
# 绘制柱状图
st.subheader(' 柱状图示例 ')
st.bar_chart(data)
# 绘制散点图
st.subheader(' 散点图示例 ')
st.scatter_chart(data)