import streamlit as st
import pandas as pd
# 创建示例数据框
data = {
 'Year': [2010, 2011, 2012, 2013, 2014],
 'Sales': [100, 150, 200, 250, 300]
}
df = pd.DataFrame(data)
# 添加折线图
st.line_chart(df.set_index('Year'))
# 添加柱状图
st.bar_chart(df.set_index('Year'))