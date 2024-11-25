import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 创建一个随机数据集
data = pd.DataFrame(np.random.randn(1000, 2), columns=['A', 'B'])
# 显示数据的统计摘要
st.write(data.describe())
# 添加侧边栏参数调整选项
st.sidebar.subheader(' 参数调整 ')
feature = st.sidebar.radio(' 选择特征 ', ('A', 'B'))
range_slider = st.sidebar.slider(' 选择范围 ', data[feature].min(), data[feature].max(), (data[feature].min(), 
data[feature].max()))
# 根据用户选择的参数过滤数据
filtered_data = data[(data[feature] >= range_slider[0]) & (data[feature] <= range_slider[1])]
# 绘制散点图
st.subheader(' 特征关系可视化 ')
# 创建一个 Figure 对象
fig = plt.figure()
# 在 Figure 对象中绘制散点图
ax = fig.add_subplot(111)
sns.scatterplot(x='A', y='B', data=filtered_data, ax=ax)
# 将 Figure 对象传递给 st.pyplot() 函数
st.pyplot(fig)