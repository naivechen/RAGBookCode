import numpy as np
# 定义两个向量
p = np.array([1, 2, 3])
q = np.array([4, 5, 6])
# 计算欧式距离
euclidean_distance = np.sqrt(np.sum((q - p) ** 2))
print(" 向量 p：", p)
print(" 向量 q：", q)
print(" 欧式距离：", euclidean_distance)