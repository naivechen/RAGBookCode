import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 创建一个随机数据集
data = pd.DataFrame(np.random.randn(1000, 2), columns=['A', 'B'])
# 显示数据的统计摘要
st.write(data.describe())
# 绘制散点图和线图
st.subheader(' 特征关系可视化 ')
# 创建一个 Figure 对象
fig = plt.figure()
# 在 Figure 对象中绘制散点图
ax1 = fig.add_subplot(121)
sns.scatterplot(x='A', y='B', data=data, ax=ax1)
# 在 Figure 对象中绘制线图
ax2 = fig.add_subplot(122)
sns.lineplot(data=data, ax=ax2)
# 将 Figure 对象传递给 st.pyplot() 函数
st.pyplot(fig)