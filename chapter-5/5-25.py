import gradio as gr

def greet(name):
    return f"Hello, {name}!"

gr.Interface(greet, gr.Textbox(label="Name"), gr.Textbox(label="Greeting")).launch()