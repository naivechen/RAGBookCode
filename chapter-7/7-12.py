from annoy import AnnoyIndex
# 创建一个 Annoy 树
dimension = 10 # 向量维度
num_trees = 10 # 树的数量
annoy_index = AnnoyIndex(dimension, 'euclidean')
# 添加示例数据
for i in range(1000):
    vector = [i * 0.1 for i in range(dimension)]
    annoy_index.add_item(i, vector)
# 构建 Annoy 树
annoy_index.build(num_trees)
# 定义查询向量
query_vector = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# 搜索最近邻
nearest_neighbors = annoy_index.get_nns_by_vector(query_vector, 5)
# 输出结果，每次结果不一定一致，因为随机
print(" 最近邻索引：", nearest_neighbors)