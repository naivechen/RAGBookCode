import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import TensorDataset, DataLoader
# 加载数据集
train_texts = [
 "I love this movie, it's the best one I've seen in years.",
 "The acting was terrible and the plot made no sense.",
 "This is my favorite movie of all time, I can watch it over and over again.",
 "I was really disappointed with this movie, it didn't live up to my expectations.",
 "The cinematography was stunning and the performances were top-notch.",
 "I hated this movie, it was a complete waste of my time.",
 "The action scenes were amazing and the story was engaging.",
 "I found this movie to be boring and predictable.",
 "This movie made me laugh so hard, I couldn't stop.",
 "The dialogue was cheesy and the characters were unlikable."
]
train_labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
train_input_ids = []
train_attention_masks = []
for text in train_texts:
    encoded = tokenizer.encode_plus(
    text,
    add_special_tokens=True,
    max_length=128,
    padding='max_length',
    truncation=True,
    return_attention_mask=True,
    return_tensors='pt'
    )
    train_input_ids.append(encoded['input_ids'])
    train_attention_masks.append(encoded['attention_mask'])

train_input_ids = torch.cat(train_input_ids, dim=0)
train_attention_masks = torch.cat(train_attention_masks, dim=0)
train_labels = torch.tensor(train_labels)
train_dataset = TensorDataset(train_input_ids, train_attention_masks, train_labels)
train_dataloader = DataLoader(train_dataset, batch_size=32)
# 定义模型和优化器
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)

# 训练模型
model.train()
for epoch in range(5):
    total_loss = 0
    for step, batch in enumerate(train_dataloader):
        batch_input_ids = batch[0]
        batch_attention_masks = batch[1]
        batch_labels = batch[2]
        optimizer.zero_grad()
        outputs = model(batch_input_ids, attention_mask=batch_attention_masks, labels= batch_labels)
        loss = outputs.loss
        total_loss += loss.item()
        loss.backward()
        optimizer.step()
    avg_loss = total_loss / len(train_dataloader)
    print(f'Epoch {epoch + 1}, average loss: {avg_loss:.4f}')

# 保存模型
torch.save(model.state_dict(), 'bert_model.pth')