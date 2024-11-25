import torch
from transformers import BertForSequenceClassification, BertTokenizer
# 加载模型和词汇表
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
# 加载模型参数
model.load_state_dict(torch.load('bert_model.pth'))
# 使用模型进行推理
text = 'this is a test sentence'
encoded = tokenizer.encode_plus(
 text,
 add_special_tokens=True,
 max_length=128,
 padding='max_length',
return_attention_mask=True,
return_tensors='pt'
)
input_ids = encoded['input_ids']
attention_mask = encoded['attention_mask']

# 模型推理
with torch.no_grad():
    output = model(input_ids, attention_mask=attention_mask)
    logits = output.logits
    probabilities = torch.softmax(logits, dim=1)
# 打印结果
print('Logits:', logits)
print('Probabilities:', probabilities)