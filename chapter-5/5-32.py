import gradio as gr
from nltk.classify import SklearnClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('movie_reviews')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from sklearn.ensemble import RandomForestClassifier

def load_model():
    docs = [(list(movie_reviews.words(fileid)), category)
        for category in movie_reviews.categories()
        for fileid in movie_reviews.fileids(category)]
    train_data, test_data = docs[:1600], docs[1600:]
    vectorizer = CountVectorizer()
    train_features = vectorizer.fit_transform([" ".join(word_tokenize(" ".join(d))) for (d, _) in train_data])
    test_features = vectorizer.transform([" ".join(word_tokenize(" ".join(d))) for (d, _) in test_data])
    classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    classifier.fit(train_features, [label for (_, label) in train_data])
    accuracy = classifier.score(test_features, [label for (_, label) in test_data])
    print("Model accuracy:", accuracy)
    return classifier, vectorizer

# 定义文本分类函数
def classify_text(text):
    # 加载预训练的文本分类模型
    classifier, vectorizer = load_model()
    # 对文本进行预处理
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(text)
    words = [lemmatizer.lemmatize(word.lower()) for word in words if word.lower() not in stop_words]
    features = vectorizer.transform([" ".join(words)])
    # 使用预训练的文本分类模型对文本进行分类
    label = classifier.predict(features)[0]
    if label == "pos":
        return " 好的 "
    else:
        return " 坏的 "
    
# 创建 Gradio 接口
interface = gr.Interface(fn=classify_text,
 inputs="text",
 outputs="label",
 title=" 文本分类 ",
 description=" 输入一段文本，判断它是好的还是坏的。")

# 启动 Gradio 应用
interface.launch()