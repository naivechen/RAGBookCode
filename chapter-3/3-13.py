import torch
import torch.nn as nn
class SelfAttention(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super(SelfAttention, self).__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim

        # 定义查询、键和值的线性变换矩阵
        self.W_q = nn.Linear(input_dim, hidden_dim)
        self.W_k = nn.Linear(input_dim, hidden_dim)
        self.W_v = nn.Linear(input_dim, hidden_dim)

    def forward(self, X):
        # 计算查询、键和值
        Q = self.W_q(X)
        K = self.W_k(X)
        V = self.W_v(X)
        # 计算注意力分数
        attention_scores = torch.matmul(Q, K.transpose(-2, -1)) / torch.sqrt(torch.tensor(self.hidden_dim, dtype=torch.float32))
        attention_weights = torch.softmax(attention_scores, dim=-1)

        # 加权求和
        output = torch.matmul(attention_weights, V)

        return output
# 测试代码
input_dim = 512
hidden_dim = 64
seq_length = 10
batch_size = 32
# 创建一个输入序列
X = torch.randn(batch_size, seq_length, input_dim)
# 创建 Self-Attention 模块
self_attention = SelfAttention(input_dim, hidden_dim)
# 应用 Self-Attention 模块
output = self_attention(X)
print("Output shape:", output.shape)