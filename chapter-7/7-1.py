# 导入必要的库
from gensim import corpora
from gensim.models import TfidfModel
from gensim.similarities import MatrixSimilarity
# 假设我们有一组文档
documents = ["This is the first document",
 "This document is the second document",
 "And this is the third one",
 "Is this the first document"]
# 将文档转换为词袋表示
texts = [[word for word in document.lower().split()] for document in documents]
# 构建词典
dictionary = corpora.Dictionary(texts)
# 构建语料库
corpus = [dictionary.doc2bow(text) for text in texts]
# 计算 TF-IDF 权重
tfidf = TfidfModel(corpus)
# 构建索引
index = MatrixSimilarity(tfidf[corpus])
# 查询
query = "first document"
query_bow = dictionary.doc2bow(query.lower().split())
query_tfidf = tfidf[query_bow]
# 获取相似度
sims = index[query_tfidf]
# 输出相似度排名
for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
    print(f"Document {document_number + 1}: {score}")