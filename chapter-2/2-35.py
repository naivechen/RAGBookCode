from torch.utils.data import DataLoader
import torchvision.datasets as datasets
# 加载 MNIST 数据集
mnist_trainset = datasets.MNIST(root='./data', train=True, download=True, transform=None)
mnist_testset = datasets.MNIST(root='./data', train=False, download=True, transform=None)
# 创建数据加载器实例
train_loader = DataLoader(dataset=mnist_trainset, batch_size=64, shuffle=True)
test_loader = DataLoader(dataset=mnist_testset, batch_size=64, shuffle=False)