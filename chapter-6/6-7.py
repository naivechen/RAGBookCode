from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
def extract_features(texts):
    # 使用 TF-IDF 向量化文本
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    return X

# 示例文本
texts = [" 这是一个示例文本，用于演示文本特征提取的过程。", " 这是另一个示例文本，用于演示文本特征提取的过程。"]
# 提取文本特征
features = extract_features(texts)
from sklearn.svm import OneClassSVM
from sklearn.metrics import accuracy_score
def train_model(X, y):
    # 将数据切分为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # 训练 OneClassSVM 类型
    model = OneClassSVM()
    model.fit(X_train)
    # 在测试集上评估模型
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return model, accuracy

# 示例特征和标签
X = features
y = [0, 0] # 示例标签，两个样本都属于 class 0
# 训练模型
trained_model, accuracy = train_model(X, y)
# 打印模型准确率
print("Model accuracy:", accuracy)