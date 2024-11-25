import gradio as gr
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 加载示例数据
iris = sns.load_dataset('iris')
# 定义数据可视化函数
def visualize_data(x_axis, y_axis, hue):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=iris, x=x_axis, y=y_axis, hue=hue)
    plt.title(f"Scatter Plot of {x_axis} vs {y_axis}")
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.legend(title=hue)
    plt.tight_layout()
    # 保存图像到文件中
    img_path = 'scatter_plot.png'
    plt.savefig(img_path)
    return img_path

# 创建 Gradio 接口
interface = gr.Interface(fn=visualize_data,
 inputs=[gr.Dropdown(choices=list(iris.columns), label="X Axis"),
 gr.Dropdown(choices=list(iris.columns), label="Y Axis"),
 gr.Dropdown(choices=list(iris.columns), label="Hue (Color)")],
 outputs=gr.Image(label="Scatter Plot"),
 title="Data Visualization",
 description="Select X and Y axes to visualize data.")

# 启动 Gradio 应用
interface.launch()