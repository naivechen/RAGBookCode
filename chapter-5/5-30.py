import pandas as pd
import gradio as gr
# 创建数据
data = {
 "Name": ["Alice", "Bob", "Charlie", "David"],
 "Age": [25, 30, 35, 40],
 "Salary": [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)

# 创建 Gradio 接口
interface = gr.Interface(fn=lambda: df,
 inputs=None,
 outputs=gr.Dataframe(),
 title="Employee Data Table",
 description="Explore employee data in the table.")

# 启动 Gradio 应用
interface.launch()