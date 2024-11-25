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
# 加载测试数据集
testset = datasets.MNIST('data/', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)
