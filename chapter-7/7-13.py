import numpy as np
from datasketch import MinHash, MinHashLSH
# 创建示例数据
X = np.random.rand(1000, 10)
# 定义 MinHashLSH 参数
num_perm = 128
threshold = 0.5
# 将数据转换为 MinHash 签名
mhs = [MinHash(num_perm=num_perm) for _ in range(len(X))]
for i, x in enumerate(X):
    mhs[i].update(str(hash(tuple(x))).encode('utf-8'))

# 构建 MinHashLSH 索引
lsh = MinHashLSH(threshold=threshold, num_perm=num_perm)
for i, mh in enumerate(mhs):
    lsh.insert(str(i), mh)

# 定义查询向量
query_index = np.random.randint(len(X))
query_vector = X[query_index]
query_mh = mhs[query_index]
# 搜索最近邻
candidates = lsh.query(query_mh)
# 计算距离并按距离排序
distances = []
for i in candidates:
    dist = np.linalg.norm(X[int(i)] - query_vector)
    distances.append((int(i), dist))
    
distances.sort(key=lambda x: x[1])
# 打印结果
num_neighbors = 5
print(" 最近邻索引：", [d[0] for d in distances[:num_neighbors]])
print(" 对应距离：", [d[1] for d in distances[:num_neighbors]])