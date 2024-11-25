import pandas as pd
import seaborn as sns
import gradio as gr

# 加载示例数据集
iris = sns.load_dataset('iris')
# 定义数据分析函数
def analyze_data(sepal_length, sepal_width, petal_length, petal_width):
    # 进行数据分析
    selected_data = iris[(iris['sepal_length'] > sepal_length) &
    (iris['sepal_width'] > sepal_width) &
    (iris['petal_length'] > petal_length) &
    (iris['petal_width'] > petal_width)]
    # 返回分析结果
    return selected_data

# 创建 Gradio 接口
interface = gr.Interface(analyze_data, 
 ["number", "number", "number", "number"], 
 "dataframe",
 title="Iris Data Analysis Tool",
 description="Explore Iris dataset by adjusting parameters.")

# 启动 Gradio 应用
interface.launch()