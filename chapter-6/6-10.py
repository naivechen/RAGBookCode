import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torch.nn.utils.rnn import pad_sequence
class CustomTokenizer:
    def __init__(self):
        self.word_index = {}
        self.index_word = {}
        self.vocab_size = 0

    def fit_on_texts(self, texts):
        for text in texts:
            for word in text.split():
                if word not in self.word_index:
                    self.word_index[word] = self.vocab_size
                    self.index_word[self.vocab_size] = word
                    self.vocab_size += 1
 
    def texts_to_sequences(self, texts):
        sequences = []
        for text in texts:
            sequence = [self.word_index[word] for word in text.split()]
            sequences.append(sequence)
        return sequences
    
# 假设已经准备好了训练数据，包括文档内容和对应的标签
# 文档内容
documents = [" 文档 1 的内容 ", " 文档 2 的内容 "," 文档 N 的内容 "]
# 文档标签
labels = [" 标签 1", " 标签 2"," 标签 N"]
# 文本分词
tokenizer = CustomTokenizer()
tokenizer.fit_on_texts(documents)
# 标签转换为数字编码
label_dict = {label: i for i, label in enumerate(set(labels))}
num_classes = len(label_dict)
numeric_labels = [label_dict[label] for label in labels]

# 构建数据集
class CustomDataset(Dataset):
    def __init__(self, documents, labels, tokenizer):
        self.documents = documents
        self.labels = labels
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.documents)

    def __getitem__(self, idx):
        document = self.documents[idx]
        label = self.labels[idx]

        sequence = self.tokenizer.texts_to_sequences([document])[0]

        return torch.tensor(sequence), torch.tensor(label)

dataset = CustomDataset(documents, numeric_labels, tokenizer)
# 构建数据加载器
batch_size = 32
data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# 构建模型，定义损失函数和优化器，训练模型等与之前相同，不再重复
# 构建模型
class LSTMModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, num_classes):
        super(LSTMModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm1 = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
        self.lstm2 = nn.LSTM(hidden_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, num_classes)
        
    def forward(self, x):
        embedded = self.embedding(x)
        output1, _ = self.lstm1(embedded)
        output2, _ = self.lstm2(output1)
        last_output = output2[:, -1, :]
        return self.fc(last_output)

vocab_size = len(tokenizer.word_index) + 1
embedding_dim = 100
hidden_dim = 64
model = LSTMModel(vocab_size, embedding_dim, hidden_dim, num_classes)
# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters())
# 训练模型
num_epochs = 10
for epoch in range(num_epochs):
    total_loss = 0
    total_correct = 0
    total_samples = 0

    for sequences, labels in data_loader:
        optimizer.zero_grad()

        predictions = model(sequences)
        loss = criterion(predictions, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        _, predicted_labels = torch.max(predictions, 1)
        total_correct += (predicted_labels == labels).sum().item()
        total_samples += labels.size(0)

        accuracy = total_correct / total_samples
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {total_loss:.4f}, Accuracy: {accuracy:.4f}')