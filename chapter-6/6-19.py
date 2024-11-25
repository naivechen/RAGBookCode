from gensim.models import FastText
import numpy as np
# 示例文本语料库
corpus = [
 ["this", "is", "a", "sample", "sentence"],
 ["fasttext", "is", "a", "word", "embedding", "technique"],
 ["it", "breaks", "words", "into", "subwords"]
]
# 训练 fastText 模型
model = FastText(sentences=corpus, vector_size=10, window=5, min_count=1, workers=4)
# 将单词向量聚合成文档向量的方法（平均池化法）
def average_pooling(doc_tokens, model):
    word_vectors = []
    for token in doc_tokens:
        word_vectors.append(model.wv[token])
    if len(word_vectors) > 0:
        doc_vector = np.mean(word_vectors, axis=0)
    else:
        doc_vector = np.zeros(model.vector_size)
    return doc_vector
# 示例文档
document = ["fasttext", "is", "a", "technique"]
# 计算文档向量
doc_vector = average_pooling(document, model)
# 打印文档向量
print("Document Vector:")
print(doc_vector)