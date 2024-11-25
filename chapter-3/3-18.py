import torch
import torch.nn as nn
import torch.optim as optim
# 创建一个简单的线性回归模型
class LinearRegression(nn.Module):
    def __init__(self, input_size, output_size):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(input_size, output_size)

    def forward(self, x):
        return self.linear(x)

# 定义训练数据
x_train = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y_train = torch.tensor([[2.0], [4.0], [6.0], [8.0]])
# 初始化模型和损失函数
input_size = 1
output_size = 1
model = LinearRegression(input_size, output_size)
criterion = nn.MSELoss()
# 初始化优化器
learning_rate = 0.01
# 使用 SGD 优化器
optimizer_sgd = optim.SGD(model.parameters(), lr=learning_rate)
# 使用 Adam 优化器
optimizer_adam = optim.Adam(model.parameters(), lr=learning_rate)
# 训练模型（使用 SGD 优化器）
num_epochs = 1000
for epoch in range(num_epochs):
    optimizer_sgd.zero_grad()
    outputs = model(x_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer_sgd.step()
    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}')

# 训练模型（使用 Adam 优化器）
for epoch in range(num_epochs):
    optimizer_adam.zero_grad()
    outputs = model(x_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer_adam.step()
    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}')