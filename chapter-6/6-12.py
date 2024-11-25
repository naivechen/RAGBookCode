from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
# 假设有一些情感分析数据，包括文本和标签
texts = [
 ' 这部电影太棒了！ ',
 ' 这个产品质量很差。',
 ' 我非常喜欢这个餐厅。',
 ' 这本书太无聊了。',
 ' 这个手机性能很好。',
 ' 这个游戏太难了。'
]
labels = [' 正面 ', ' 负面 ', ' 正面 ', ' 负面 ', ' 正面 ', ' 负面 ']
# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)
# 初始化词袋模型
vectorizer = CountVectorizer()
# 训练文档向量化器
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
# 初始化朴素贝叶斯分类器
classifier = MultinomialNB()
# 训练分类器
classifier.fit(X_train_vec, y_train)
# 在测试集上进行预测
y_pred = classifier.predict(X_test_vec)
# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(" 准确率：", accuracy)