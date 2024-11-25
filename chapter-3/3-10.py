import torch
import torch.nn as nn
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    def forward(self, x):
        # 初始化隐藏状态
        h0 = torch.zeros(1, x.size(0), self.hidden_size).to(x.device)
        # RNN 前向计算
        out, _ = self.rnn(x, h0)
        # 只取最后一个时间步的输出
        out = self.fc(out[:, -1, :])
        return out
# 定义输入、隐藏状态和输出的维度
input_size = 10
hidden_size = 20
output_size = 2
# 创建 RNN 模型
rnn_model = SimpleRNN(input_size, hidden_size, output_size)
print(rnn_model)