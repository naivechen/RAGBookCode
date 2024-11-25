import nltk
def text_preprocessing(text):
    # 切分文本为句子
    sentences = nltk.sent_tokenize(text)
    return sentences

# 示例文本
text = "Natural language processing is an important technology. It can be used in many fields, such as machine translation, sentiment analysis, speech recognition, etc. Document chunking is a key step in natural language processing. It helps us better understand and organize text data."
# 使用文本预处理进行文本切分
sentences = text_preprocessing(text)
# 打印切分结果
for i, sentence in enumerate(sentences):
    print(f"Sentence {i+1}: {sentence}")