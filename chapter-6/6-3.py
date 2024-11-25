import re
def text_segmentation(text):
    # 使用正则表达式切分文本
    sentences = re.split(r'[。！？；]', text)
    return sentences

# 示例文本
text = "这是一个示例文本，用于演示文本切分的算法。文本切分可以根据句子边界或标点符号将文本分割成不同的段落。"
# 使用文本切分进行分块
sentences = text_segmentation(text)
# 打印分块结果
for i, sentence in enumerate(sentences):
    print(f"Sentence {i+1}: {sentence}")