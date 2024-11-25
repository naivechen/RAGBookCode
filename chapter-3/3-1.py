import torch
import torch.nn as nn
# 定义感知机模型
class Perceptron(nn.Module):
    def __init__(self, input_size):
        super(Perceptron, self).__init__()
        self.fc = nn.Linear(input_size, 1) # 输入大小为 input_size，输出大小为 1
        self.sigmoid = nn.Sigmoid() # 使用 sigmoid 作为激活函数

    def forward(self, x):
        out = self.fc(x)
        out = self.sigmoid(out)
        return out

# 创建感知机模型
input_size = 2 # 输入特征的维度
model = Perceptron(input_size)
# 打印模型结构
print(model)