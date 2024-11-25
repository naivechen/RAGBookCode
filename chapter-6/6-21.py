from transformers import BertTokenizer, BertModel
import torch
# 加载预训练的 BERT 模型和分词器
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
# 示例文本
text = "Here is the sample text we want to encode into a document vector."
# 文本分词和编码
input_ids = tokenizer.encode(text, add_special_tokens=True, max_length=512, truncation=True, return_tensors='pt')
# 获取模型输出
with torch.no_grad():
    outputs = model(input_ids)
# 提取 CLS 向量作为文档向量
document_vector = outputs.last_hidden_state[:, 0, :].squeeze().numpy()
# 打印文档向量
print("Document Vector:")
print(document_vector)