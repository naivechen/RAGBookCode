from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from scipy.stats import pearsonr
from sklearn.cluster import KMeans
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
# 指定要包含的类别
categories = ['alt.atheism', 'talk.religion.misc']
# 加载较小的子集
newsgroups_train = fetch_20newsgroups(subset='train', categories=categories)
# 使用 TF-IDF 向量化器将文本转换为向量
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(newsgroups_train.data)
# 计算文档之间的余弦相似度
cos_sim = cosine_similarity(X)
# 计算文档之间的欧氏距离
euclidean_dist = euclidean_distances(X)
# 计算文档之间的 Pearson 相关系数
pearson_corr = pearsonr(X.toarray()[0], X.toarray()[1])
# 使用 K 均值算法对文档进行聚类
kmeans = KMeans(n_clusters=20)
kmeans.fit(X)
labels = kmeans.labels_
# 计算聚类准确度
cluster_acc = sum(labels == newsgroups_train.target) / len(labels)
# 打印评估结果
print("Cosine Similarity: ", cos_sim)
print("Euclidean Distance: ", euclidean_dist)
print("Pearson Correlation Coefficient: ", pearson_corr)
print("Clustering Accuracy: ", cluster_acc)