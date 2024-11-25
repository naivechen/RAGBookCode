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
# 打印特征维度
print("Feature dimension:", features.shape)