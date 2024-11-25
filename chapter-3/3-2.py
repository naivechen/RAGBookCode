import torch
import torch.nn as nn
class MLP(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size) # 第一个全连接层，输入维度为
        # input_size，输出维度为 hidden_size
        self.relu = nn.ReLU() # ReLU 激活函数
        self.fc2 = nn.Linear(hidden_size, output_size) # 第二个全连接层，输入维度为
        # hidden_size，输出维度为 output_size

    def forward(self, x):
        out = self.fc1(x) # 输入经过第一个全连接层
        out = self.relu(out) # 经过 ReLU 激活函数
        out = self.fc2(out) # 再经过第二个全连接层
        return out

# 创建一个输入维度为 10，隐藏层维度为 20，输出维度为 1 的多层感知机模型
model = MLP(input_size=10, hidden_size=20, output_size=1)
print(model) # 打印模型结构