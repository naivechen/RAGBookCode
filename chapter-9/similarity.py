# 代码 9-4

import numpy as np
from vector import get_embedding


def get_cos_similarity(p, q):
    # 计算余弦距离
    cosine_similarity = np.dot(p, q) / (np.linalg.norm(p) * np.linalg.norm(q))

    return cosine_similarity


def get_top_k(K, data, query):
    ret = [] # { "text": xxx, "score": xxx }
    query_embedding = get_embedding(text=query)
    # print(query_embedding)
    for text in data:
        embedding = get_embedding(text=text)
        score = get_cos_similarity(embedding, query_embedding)
        ret.append(
            {
                "text": text,
                "score": score
            }
        )

    # 按照score从大到小排序
    sorted_ret = sorted(ret, key=lambda x: x["score"], reverse=True) 

    return sorted_ret[:K]

# 样例数据
data = [
    "序号 普通股股东名称 期末持股数量 持股比例 持有有限",
    "额的百分比 数量",
    "合计 占已发行普",
    "中国工商银行－上证",
    "50交易型开放式",
    "指数证券投资基金 256,936,000 0.09% 1,694,600 0.0006% 350,230,920 0.12% - -",
    "中国工商银行股份有",
    "限公司－华泰柏瑞"
]

ret = get_top_k(K=3, data=data, query="中国工商银行－上证")
print(ret)