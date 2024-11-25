from sklearn.feature_extraction.text import TfidfVectorizer
# 示例文档
documents = [
 "This is the first document.",
 "This document is the second document.",
 "And this is the third one.",
 "Is this the first document?",
]
# 创建 TF-IDF 矩阵
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)
# 打印词汇表
print("Vocabulary: ", vectorizer.get_feature_names_out())
# 打印 TF-IDF 矩阵
print("TF-IDF Matrix: ")
print(X.toarray())