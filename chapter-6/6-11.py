from sklearn.feature_extraction.text import CountVectorizer
# 假设有一些文档数据
documents = [
 ' 这是第一个文档 ',
 ' 这是第二个文档 ',
 ' 这是第三个文档 ',
 ' 这是第四个文档 '
 ]
# 初始化词袋模型
vectorizer = CountVectorizer()
# 文档向量化
document_vectors = vectorizer.fit_transform(documents)
# 输出向量化结果
print(" 文档向量化结果：")
print(document_vectors.toarray())
# 输出词汇表
print(" 词汇表：")
print(vectorizer.get_feature_names_out())