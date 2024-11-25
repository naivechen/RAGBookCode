import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 创建一个随机数据集
data = pd.DataFrame(np.random.randn(1000, 2), columns=['A', 'B'])
# 显示数据的统计摘要
st.write(data.describe())
# 绘制直方图
st.subheader(' 数据分布可视化 ')
# 创建一个图形对象
fig, ax = plt.subplots()
sns.histplot(data['A'], kde=True, ax=ax)
st.pyplot(fig)
# 创建另一个图形对象
fig, ax = plt.subplots()
sns.histplot(data['B'], kde=True, ax=ax)
st.pyplot(fig)