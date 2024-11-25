import numpy as np
# 示例文档
document = "This is a sample document for hot encoding demonstration"
# 构建词汇表
vocab = set(document.split())
word_to_index = {word: i for i, word in enumerate(vocab)}

# Hot 编码函数
def one_hot_encoding(document, word_to_index):
    # 初始化全零向量
    one_hot_vector = np.zeros(len(word_to_index))
    # 对文档中出现的单词进行 Hot 编码
    for word in document.split():
        if word in word_to_index:
            one_hot_vector[word_to_index[word]] = 1
    return one_hot_vector

# 对示例文档进行 Hot 编码
encoded_vector = one_hot_encoding(document, word_to_index)
# 打印 Hot 编码向量
print("Hot Encoded Vector:")
print(encoded_vector)