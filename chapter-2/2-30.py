import torch
import torch.nn as nn
# 定义一个简单的神经网络模型
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(10, 5)
        self.fc2 = nn.Linear(5, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x
# 创建模型实例
model = SimpleNet()
# 访问模型参数
for name, param in model.named_parameters():
    print(f"Parameter name: {name}, Size: {param.size()}")