import nltk
def chunk_text(text, chunk_size=100):
    # 分句
    sentences = nltk.sent_tokenize(text)
    chunks = []
    chunk = "" 
    for sentence in sentences:
        if len(chunk) + len(sentence) <= chunk_size:
            chunk += " " + sentence
        else:
            chunks.append(chunk.strip())
            chunk = sentence
    if chunk:
        chunks.append(chunk.strip())
    return chunks

# 示例文本
text = "Natural language processing is an important technology. It can be used in many fields, such as machine translation, sentiment analysis, speech recognition, etc. Document chunking is a key step in natural language processing. It helps us better understand and organize text data."
# 分块处理
chunks = chunk_text(text)
print(" 分块后的文本：", chunks)
print(" 分块后的文本数量：", len(chunks))