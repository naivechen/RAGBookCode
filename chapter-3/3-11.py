import torch
import torch.nn as nn

class SimpleLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleLSTM, self).__init__()
        self.hidden_size = hidden_size
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    def forward(self, x):
        # 初始化隐藏状态和细胞状态
        h0 = torch.zeros(1, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(1, x.size(0), self.hidden_size).to(x.device)
        # LSTM 前向计算
        out, _ = self.lstm(x, (h0, c0))
        # 只取最后一个时间步的输出
        out = self.fc(out[:, -1, :])
        return out

# 定义输入、隐藏状态和输出的维度
input_size = 10
hidden_size = 20
output_size = 2
# 创建 LSTM 模型
lstm_model = SimpleLSTM(input_size, hidden_size, output_size)
print(lstm_model)