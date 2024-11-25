from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report
# 假设已经准备好了训练数据，包括文档内容和对应的标签
# 文档内容
documents = [" 文档 1 的内容 ", " 文档 2 的内容 ", " 文档 N 的内容 "]
# 文档标签
labels = [" 标签 1", " 标签 2", " 标签 N"]
# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(documents, labels, test_size=0.2, random_state=42)
# 使用 TF-IDF 特征提取
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)
# 训练支持向量机模型
svm_model = SVC(kernel='linear')
svm_model.fit(X_train_tfidf, y_train)
# 在测试集上进行预测
y_pred = svm_model.predict(X_test_tfidf)
# 输出分类报告
print(classification_report(y_test, y_pred))