from sklearn.neighbors import KDTree
import numpy as np
# 创建一组示例数据
X = np.array([[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]])
# 构建 KD- 树
kdtree = KDTree(X, leaf_size=30)
# 定义查询点
query_point = np.array([[5, 5]])
# 搜索最近邻
distances, indices = kdtree.query(query_point, k=3)
# 输出结果
print(" 最近邻点索引：", indices)
print(" 最近邻点距离：", distances)