import pandas as pd
import gradio as gr
# 创建一个示例数据表格
data = pd.DataFrame({
 'Name': ['Alice', 'Bob', 'Charlie'],
 'Age': [25, 30, 35],
 'Gender': ['Female', 'Male', 'Male']
})
gr.Interface(lambda df: df, gr.Dataframe(data), "dataframe").launch()