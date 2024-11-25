import torch
import torch.optim as optim
from torch.optim.lr_scheduler import StepLR, ExponentialLR
# 定义模型和损失函数
class LinearRegression(torch.nn.Module):
    def __init__(self, input_size, output_size):
        super(LinearRegression, self).__init__()
        self.linear = torch.nn.Linear(input_size, output_size)
    def forward(self, x):
        return self.linear(x)
    

model = LinearRegression(1, 1)
criterion = torch.nn.MSELoss()
# 定义优化器
optimizer = optim.SGD(model.parameters(), lr=0.1)
# 定义学习率调度器
# 按照步数衰减
scheduler_step = StepLR(optimizer, step_size=30, gamma=0.1)
# 按照指数衰减
scheduler_exp = ExponentialLR(optimizer, gamma=0.95)
# 训练模型
num_epochs = 10
for epoch in range(num_epochs):
    # 执行学习率调度
    scheduler_step.step()
    # scheduler_exp.step()

    # 其他训练步骤
    optimizer.zero_grad()
    outputs = model(torch.tensor([[1.], [2.], [3.], [4.]]))
    labels = torch.tensor([[2.], [4.], [6.], [8.]])
    loss = criterion(outputs, labels)
    loss.backward()
    optimizer.step()
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}')