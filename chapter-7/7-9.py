import numpy as np
def jaccard_distance(set1, set2):
    # 计算交集和并集的元素个数
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))

    # 计算杰卡德距离
    distance = 1 - intersection / union

    return distance
# 定义两个集合
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
# 计算杰卡德距离
distance = jaccard_distance(set1, set2)
print(" 集合 1：", set1)
print(" 集合 2：", set2)
print(" 杰卡德距离：", distance)