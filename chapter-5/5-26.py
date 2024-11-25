import gradio as gr
def chatbot(text):
    # 在这里编写聊天机器人的逻辑代码
    # 返回机器人的回复
    bot_reply = "Sorry, I didn't understand that."
    # 示例逻辑：如果用户发送了 "Hello"，则回复 "Hello, how can I help you?"
    if text.lower() == "hello":
        bot_reply = "Hello, how can I help you?"
    return bot_reply

gr.Interface(chatbot, gr.Textbox(label="Enter your message"), gr.Textbox(label="Bot reply")).launch()