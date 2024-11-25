import torch
import torch.nn as nn
from torchsummary import summary
class SimpleNet(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# 指定输入维度、隐藏层维度和输出维度
input_dim = 100
hidden_dim = 50
output_dim = 10
# 创建一个 SimpleNet 模型实例
model = SimpleNet(input_dim, hidden_dim, output_dim)
# 打印模型的结构
summary(model, input_size=(input_dim,))