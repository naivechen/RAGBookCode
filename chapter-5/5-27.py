import time
import gradio as gr

def long_running_task(input_text):
    # 模拟一个耗时的任务
    time.sleep(5)
    return "Task completed!"

gr.Interface(long_running_task, gr.Textbox(label="Status"), gr.Textbox(label="Result")).launch()