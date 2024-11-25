import torch
import torch.nn as nn
class SimpleGRU(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleGRU, self).__init__()
        self.hidden_size = hidden_size
        self.gru = nn.GRU(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    def forward(self, x):
        # 初始化隐藏状态
        h0 = torch.zeros(1, x.size(0), self.hidden_size).to(x.device)
        # GRU 前向计算
        out, _ = self.gru(x, h0)
        # 只取最后一个时间步的输出
        out = self.fc(out[:, -1, :])
        return out

# 定义输入、隐藏状态和输出的维度
input_size = 10
hidden_size = 20
output_size = 2
# 创建 GRU 模型
gru_model = SimpleGRU(input_size, hidden_size, output_size)
print(gru_model)