import torch
import torch.nn as nn
import torch.optim as optim
# 定义多层感知机模型
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

# 准备数据
input_size = 10
hidden_size = 20
output_size = 1
num_samples = 100
x = torch.randn(num_samples, input_size) # 输入数据
y = torch.randn(num_samples, output_size) # 真实标签

# 创建模型、损失函数和优化器
model = MLP(input_size, hidden_size, output_size)
criterion = nn.MSELoss() # 均方误差损失函数
optimizer = optim.SGD(model.parameters(), lr=0.01) # 随机梯度下降优化器
# 训练模型
num_epochs = 100
for epoch in range(num_epochs):
    # 前向传播
    outputs = model(x)
    loss = criterion(outputs, y)
    # 反向传播
    optimizer.zero_grad() # 梯度清零
    loss.backward() # 反向传播
    optimizer.step() # 更新参数

    # 每 10 个 epoch 打印一次损失值
    if (epoch+1) % 10 == 0:
        print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))