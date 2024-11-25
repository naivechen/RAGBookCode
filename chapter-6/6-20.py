from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from nltk.tokenize import word_tokenize
# 示例文本语料库
corpus = [
 "This is the first document",
 "This document is the second document",
 "And this is the third one",
 "Is this the first document"
]
# 对文档进行分词和标记
tagged_data = [TaggedDocument(words=word_tokenize(doc.lower()), tags=[str(i)]) for i, doc in enumerate(corpus)]
# 训练 Doc2Vec 模型
model = Doc2Vec(vector_size=10, window=2, min_count=1, workers=4, epochs=20)
model.build_vocab(tagged_data)
model.train(tagged_data, total_examples=model.corpus_count, epochs=model.epochs)
# 获取文档向量
doc_vector = model.docvecs['0'] # 获取第一个文档的向量表示
# 打印文档向量
print("Document Vector:")
print(doc_vector)