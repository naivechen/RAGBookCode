import gradio as gr

def toggle(value):
    if value:
        return "Toggle is ON"
    else:
        return "Toggle is OFF"
    
gr.Interface(toggle, gr.Checkbox(label="Toggle"), gr.Textbox(label="Status")).launch()