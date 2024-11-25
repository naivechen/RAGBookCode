import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
# 定义一个包含多头自注意力机制的模块
class MultiHeadAttention(nn.Module):
    def __init__(self, embed_dim, num_heads):
        super(MultiHeadAttention, self).__init__()
        self.num_heads = num_heads
        self.embed_dim = embed_dim
        assert embed_dim % num_heads == 0
        self.head_dim = embed_dim // num_heads

        self.query_linear = nn.Linear(embed_dim, embed_dim)
        self.key_linear = nn.Linear(embed_dim, embed_dim)
        self.value_linear = nn.Linear(embed_dim, embed_dim)
        self.output_linear = nn.Linear(embed_dim, embed_dim)

    def forward(self, query, key, value):
        # 拆分成多个头
        batch_size = query.shape[0]
        query = self.query_linear(query).view(batch_size, -1, self.num_heads, self.head_dim).permute(0, 2, 1, 3)
        key = self.key_linear(key).view(batch_size, -1, self.num_heads, self.head_dim).permute(0, 2, 1, 3)
        value = self.value_linear(value).view(batch_size, -1, self.num_heads, self.head_dim).permute(0, 2, 1, 3)

        # 计算注意力分数
        energy = torch.matmul(query, key.permute(0, 1, 3, 2)) / np.sqrt(self.head_dim)

        # 注意力权重
        attention = torch.softmax(energy, dim=-1)

        # 加权求和
        out = torch.matmul(attention, value)

        # 合并多头结果
        out = out.permute(0, 2, 1, 3).contiguous().view(batch_size, -1, self.embed_dim)

        # 线性变换
        out = self.output_linear(out)

        return out

# 定义一个 Transformer 编码器层
class TransformerEncoderLayer(nn.Module):
    def __init__(self, embed_dim, num_heads):
        super(TransformerEncoderLayer, self).__init__()
        self.self_attention = MultiHeadAttention(embed_dim, num_heads)
        self.linear1 = nn.Linear(embed_dim, embed_dim)
        self.linear2 = nn.Linear(embed_dim, embed_dim)
        self.norm1 = nn.LayerNorm(embed_dim)
        self.norm2 = nn.LayerNorm(embed_dim)
 
    def forward(self, x):
        attention_out = self.self_attention(x, x, x)
        x = x + attention_out
        x = self.norm1(x)
        linear_out = self.linear2(torch.relu(self.linear1(x)))
        x = x + linear_out
        x = self.norm2(x)
        return x
    
# 定义一个 Transformer 模型
class TransformerEncoder(nn.Module):
    def __init__(self, num_layers, embed_dim, num_heads):
        super(TransformerEncoder, self).__init__()
        self.layers = nn.ModuleList([TransformerEncoderLayer(embed_dim, num_heads) for _ in range(num_layers)])

    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

# 测试模型
embed_dim = 512
num_heads = 8
num_layers = 6
sequence_length = 10
batch_size = 16
# 随机生成输入序列
input_sequence = torch.randn(batch_size, sequence_length, embed_dim)
# 构建 Transformer 模型
transformer = TransformerEncoder(num_layers, embed_dim, num_heads)
# 前向传播
output_sequence = transformer(input_sequence)
print(" 输入序列形状：", input_sequence.shape)
print(" 输出序列形状：", output_sequence.shape)