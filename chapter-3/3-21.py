import torch
import torch.nn as nn
# 定义模型
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.fc1 = nn.Linear(10, 100)
        self.dropout = nn.Dropout(p=0.5) # 添加 Dropout 层
        self.fc2 = nn.Linear(100, 10)
        self.bn = nn.BatchNorm1d(100) # 添加 Batch Normalization 层

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.bn(x)
        x = self.fc2(x)
        return x

# 创建模型实例
model = Model()
print(model)