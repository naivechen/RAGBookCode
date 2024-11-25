import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import torchvision.datasets as datasets
# 加载 MNIST 数据集
mnist_trainset = datasets.MNIST(root='./data', train=True, download=True, transform=None)
mnist_testset = datasets.MNIST(root='./data', train=False, download=True, transform=None)
# 创建数据加载器实例
train_loader = DataLoader(dataset=mnist_trainset, batch_size=64, shuffle=True)
test_loader = DataLoader(dataset=mnist_testset, batch_size=64, shuffle=False)


# 定义数据标准化的转换操作
transform = transforms.Compose([
 transforms.ToTensor(), # 将数据转换为张量
 transforms.Normalize((0.5,), (0.5,)) # 标准化操作
])
# 转换操作应用到数据集
trainset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)

# 定义数据增强的转换操作
transform = transforms.Compose([
 transforms.RandomRotation(10), # 随机旋转角度范围为 ±10 度
 transforms.RandomCrop(28, padding=4), # 随机裁剪并填充
 transforms.RandomHorizontalFlip(), # 随机水平翻转
 transforms.ToTensor(), # 将数据转换为张量
 transforms.Normalize((0.5,), (0.5,)) # 标准化操作
])
# 数据增强转换操作应用到数据集
trainset = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)