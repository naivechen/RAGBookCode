import streamlit as st
import pandas as pd
# 创建示例数据框
data = {
 'Name': ['Alice', 'Bob', 'Charlie'],
 'Age': [25, 30, 35],
 'Gender': ['Female', 'Male', 'Male']
}
df = pd.DataFrame(data)
# 添加数据表格
st.dataframe(df)