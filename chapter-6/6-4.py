from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
def topic_based_chunking(texts, num_clusters):
    # 使用 TF-IDF 向量化文本
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    # 使用 K 均值聚类算法进行文本分块
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(X)
    # 获取文档分块结果
    clusters = {}
    for i, label in enumerate(kmeans.labels_):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(texts[i])
    return clusters

# 示例文本
texts = [" 这是一篇关于自然语言处理的文章。", " 这是一篇关于机器学习的文章。", " 这是一篇关于计算机视觉的文章。"]
# 使用基于主题的分块进行文本分块
num_clusters = 2
clusters = topic_based_chunking(texts, num_clusters)
# 打印分块结果
for cluster_id, texts in clusters.items():
    print(f"Cluster {cluster_id+1}:")
    for text in texts:
        print(text)
    print()