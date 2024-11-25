import gradio as gr
import pandas as pd
import numpy as np
import sweetviz as sv
# 生成随机数据
np.random.seed(0)
data = pd.DataFrame({
 'A': np.random.randint(0, 10, 100),
 'B': np.random.randn(100),
 'C': np.random.choice(['cat', 'dog', 'fish'], 100),
 'D': np.random.choice(['low', 'medium', 'high'], 100)
})
# 定义数据报告生成函数
def generate_report(data, report_format):
    # 生成报告
    report = sv.analyze(data)
    # 输出报告
    if report_format == "HTML":
        report.show_html('report.html')
        return "Report generated successfully! Please check report.html."
    elif report_format == "JSON":
        report.show_json('report.json')
        return "Report generated successfully! Please check report.json."
    else:
        return "Invalid report format. Please choose HTML or JSON."

# 创建 Gradio 接口
interface = gr.Interface(fn=generate_report,
 inputs=[gr.Dataframe(label="Upload Dataframe"),
 gr.Radio(choices=["HTML", "JSON"], label="Report Format")],
 outputs="text",
 title="Data Report Generation",
 description="Upload a Dataframe and choose report format to generate report.")
# 启动 Gradio 应用
interface.launch()