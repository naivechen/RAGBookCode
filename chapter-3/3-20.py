import torch
import torch.nn as nn
import torch.optim as optim

# 定义模型
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)

# 创建模型实例
model = Model()
# 定义损失函数
criterion = nn.MSELoss()

# 定义优化器，并添加正则化项
optimizer = optim.SGD(model.parameters(), lr=0.01, weight_decay=1e-5) # 添加 L2 正则化项
# L1 正则化，首先定义优化器，不使用 weight_decay 参数
# optimizer = optim.SGD(model.parameters(), lr=0.01)
# L1 正则化
# lambda_l1 = 1e-5
# 训练模型
num_epochs = 10
for epoch in range(num_epochs):
    optimizer.zero_grad()
    inputs = torch.randn(32, 10) # 示例输入
    targets = torch.randn(32, 1) # 示例目标
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    loss.backward()
    optimizer.step()

    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}')
    print(f'Middle result: {outputs.mean()}') # 打印中间结果