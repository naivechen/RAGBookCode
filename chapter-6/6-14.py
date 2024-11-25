from sklearn.feature_extraction.text import CountVectorizer
# 示例文档
documents = [
 "This is the first document.",
 "This document is the second document.",
 "And this is the third one.",
 "Is this the first document?",
]
# 创建词频矩阵
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)
# 打印词汇表
print("Vocabulary: ", vectorizer.get_feature_names_out())
# 打印词频矩阵
print("Word Frequency Matrix: ")
print(X.toarray())