# 代码 9-3

from transformers import BertTokenizer, BertModel
import torch

# 加载预训练的BERT模型和分词器
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def get_embedding(text):
    # 文本分词和编码
    input_ids = tokenizer.encode(text, add_special_tokens=True, max_length=512, truncation=True, return_tensors='pt')

    # 获取模型输出
    with torch.no_grad():
        outputs = model(input_ids)

    # 提取CLS向量作为文档向量
    document_vector = outputs.last_hidden_state[:, 0, :].squeeze().numpy()

    return document_vector


if __name__ == "__main__":
    # 示例文本
    text = "序号 普通股股东名称 期末持股数量 持股比例 持有有限"
    embedding = get_embedding(text=text)
    print(len(embedding))
