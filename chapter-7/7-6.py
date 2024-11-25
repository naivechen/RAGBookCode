import numpy as np
# 定义两个向量
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
# 计算向量的内积
dot_product = np.dot(A, B)
# 计算向量的范数
norm_A = np.linalg.norm(A)
norm_B = np.linalg.norm(B)
# 计算余弦相似度
cosine_similarity = dot_product / (norm_A * norm_B)
print(" 向量 A：", A)
print(" 向量 B：", B)
print(" 内积：", dot_product)
print(" 向量 A 的范数：", norm_A)
print(" 向量 B 的范数：", norm_B)
print(" 余弦相似度（内积距离）：", cosine_similarity)