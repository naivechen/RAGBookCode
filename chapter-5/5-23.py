import gradio as gr
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
def analyze_text(text):
    # 创建情感分析器
    sia = SentimentIntensityAnalyzer()
    # 对文本进行情感分析
    sentiment_scores = sia.polarity_scores(text)
    # 返回情感分析结果
    return sentiment_scores

import nltk
nltk.download('vader_lexicon')
gr.Interface(analyze_text, "text", "label").launch()