
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

from gensim import corpora
# 文本预处理，转换为词袋表示
texts = [[word for word in document.lower().split()] for document in documents]
# 构建词典
dictionary = corpora.Dictionary(texts)
# 构建语料库
corpus = [dictionary.doc2bow(text) for text in texts]