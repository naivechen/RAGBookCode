from gensim import corpora, models, similarities
# 示例文档集合
documents = [
 "Human machine interface for lab abc computer applications",
 "A survey of user opinion of computer system response time",
 "The EPS user interface management system",
 "System and human system engineering testing of EPS",
 "Relation of user perceived response time to error measurement",
 "The generation of random binary unordered trees",
 "The intersection graph of paths in trees",
 "Graph minors IV Widths of trees and well quasi ordering",
 "Graph minors A survey",
]
# 文本预处理，转换为词袋表示
texts = [[word for word in document.lower().split()] for document in documents]
# 构建词典
dictionary = corpora.Dictionary(texts)
# 构建语料库
corpus = [dictionary.doc2bow(text) for text in texts]
# 训练 TF-IDF 模型
tfidf = models.TfidfModel(corpus)
# 转换文档为 TF-IDF 矩阵
corpus_tfidf = tfidf[corpus]
# 构建索引
index = similarities.MatrixSimilarity(corpus_tfidf)
# 查询示例
query = "human computer interaction"
query_bow = dictionary.doc2bow(query.lower().split())
query_tfidf = tfidf[query_bow]
# 计算相似度
sims = index[query_tfidf]
# 输出结果
for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
    print(f"Document {document_number + 1}: {score}")