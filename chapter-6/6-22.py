from transformers import GPT2Tokenizer, GPT2Model
import torch
# 加载预训练的 GPT 模型和分词器
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')
# 示例文本
text = "Here is the sample text we want to encode into a document vector."
# 文本分词和编码
input_ids = tokenizer.encode(text, add_special_tokens=True, max_length=512, truncation=True, return_tensors='pt')
# 获取模型输出
with torch.no_grad():
    outputs = model(input_ids)
# 提取输出向量的平均值作为文档向量
document_vector = torch.mean(outputs.last_hidden_state, dim=1).squeeze().numpy()
# 打印文档向量
print("Document Vector:")
print(document_vector[:10])