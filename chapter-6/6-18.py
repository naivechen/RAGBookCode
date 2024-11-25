from gensim.models import Word2Vec
import numpy as np
# 示例文本语料库
corpus = [
 ["this", "is", "a", "sample", "sentence"],
 ["word2vec", "is", "a", "popular", "word", "embedding", "technique"],
 ["it", "maps", "words", "to", "low-dimensional", "vectors"]
 ]
# 训练 Word2Vec 模型
model = Word2Vec(sentences=corpus, vector_size=10, window=5, min_count=1, workers=4)
# 将单词向量聚合成文档向量的方法（平均池化法）
def average_pooling(doc_tokens, model):
    word_vectors = []
    for token in doc_tokens:
        if token in model.wv.key_to_index:
            word_vectors.append(model.wv[token])
    if len(word_vectors) > 0:
        doc_vector = np.mean(word_vectors, axis=0)
    else:
        doc_vector = np.zeros(model.vector_size)
    return doc_vector

# 示例文档
document = ["word2vec", "is", "a", "technique"]
# 计算文档向量
doc_vector = average_pooling(document, model)
# 打印文档向量
print("Document Vector:")
print(doc_vector)