import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor
# 加载测试数据集
test_dataset = MNIST(root='data/', train=False, transform=ToTensor(), download=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)
