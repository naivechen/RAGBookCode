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
# 显示数据摘要
st.subheader(' 数据摘要 ')
st.write(data.describe())
# 计算相关系数
st.subheader(' 相关系数矩阵 ')
st.write(data.corr())