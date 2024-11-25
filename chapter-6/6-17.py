import numpy as np
# 示例文档
document = "This is a sample document for hash encoding demonstration"
# 构建词汇表
vocab = set(document.split())
word_to_hash = {word: hash(word) for word in vocab}
# 哈希编码函数
def hash_encoding(document, word_to_hash, vector_length):
    # 初始化全零向量
    hash_vector = np.zeros(vector_length)
    # 对文档中出现的单词进行哈希编码
    for word in document.split():
        if word in word_to_hash:
            hash_index = abs(word_to_hash[word]) % vector_length
        hash_vector[hash_index] = 1
    return hash_vector

# 定义向量长度
vector_length = 10
# 对示例文档进行哈希编码
encoded_vector = hash_encoding(document, word_to_hash, vector_length)
# 打印哈希编码向量
print("Hash Encoded Vector:")
print(encoded_vector)