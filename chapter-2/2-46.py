import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F
# 定义神经网络模型
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(28*28, 128)
        self.fc2 = nn.Linear(128, 10)
        
    def forward(self, x):
        x = x.view(-1, 28*28)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

import torch
from torchvision import datasets, transforms
# 定义数据变换方法
transform = transforms.Compose([
 transforms.ToTensor(),
 transforms.Normalize((0.5,), (0.5,))
])
# 加载训练数据集
trainset = datasets.MNIST('data/', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

# 实例化模型
model = Net()
# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
# 设置训练周期
epochs = 5
# 开始训练
for epoch in range(epochs):
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data
        # 梯度清零
        optimizer.zero_grad()

        # 前向传播
        outputs = model(inputs)
        loss = criterion(outputs, labels)

        # 反向传播和优化
        loss.backward()
        optimizer.step()

        # 统计损失
        running_loss += loss.item()
        if i % 100 == 99:
            print(f"[Epoch {epoch+1}, Iteration {i+1}] Loss: {running_loss/100:.3f}")
            running_loss = 0.0

print("Finished Trainig")


import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor
# 加载测试数据集
test_dataset = MNIST(root='data/', train=False, transform=ToTensor(), download=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

def evaluate_model(model, test_loader):
    model.eval() # 设置模型为评估模式
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = correct / total
    print(f"Accuracy on test set: {accuracy:.4f}")

# 调用评估函数
evaluate_model(model, test_loader)