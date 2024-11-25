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
model1 = SimpleNet()
model2 = SimpleNet()

# 定义初始化模型参数的函数
def init_weights(m):
    if isinstance(m, nn.Linear):
        torch.nn.init.xavier_uniform_(m.weight)
        m.bias.data.fill_(0.01)
# 使用这个函数初始化模型参数
model2.apply(init_weights)

# 对比两个模型的参数
for (name1, param1), (name2, param2) in zip(model1.named_parameters(), model2.named_parameters()):
    print(f"Comparing {name1}:")
    print(f"Model 1: {param1[:5]}")  # 打印前5个值
    print(f"Model 2: {param2[:5]}")
    print(f"Difference: {(param1 - param2)[:5]}")  # 计算差值
