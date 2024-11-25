import gradio as gr

# 定义一个简单的模型函数
def predict_number(number):
    # 在这里编写模型处理输入的代码
    prediction = " 奇数 " if number % 2 != 0 else " 偶数 "
    return prediction

# 创建一个 Gradio 接口，将模型函数包装起来
gr.Interface(predict_number, "number", "label").launch()