import torch
import torch.nn as nn
# 定义 VGG 网络的特征提取部分
features = nn.Sequential(
    nn.Conv2d(3, 64, kernel_size=3, padding=1),
    nn.ReLU(True),
    nn.Conv2d(64, 64, kernel_size=3, padding=1),
    nn.ReLU(True),
    nn.MaxPool2d(kernel_size=2, stride=2),
    nn.Conv2d(64, 128, kernel_size=3, padding=1),
    nn.ReLU(True),
    nn.Conv2d(128, 128, kernel_size=3, padding=1),
    nn.ReLU(True),
    nn.MaxPool2d(kernel_size=2, stride=2),
    nn.Conv2d(128, 256, kernel_size=3, padding=1),
    nn.ReLU(True),
    nn.Conv2d(256, 256, kernel_size=3, padding=1),
    nn.ReLU(True),
    nn.Conv2d(256, 256, kernel_size=3, padding=1),
    nn.ReLU(True),
    nn.MaxPool2d(kernel_size=2, stride=2),
    nn.Conv2d(256, 512, kernel_size=3, padding=1),
    nn.ReLU(True),
    nn.Conv2d(512, 512, kernel_size=3, padding=1),
    nn.ReLU(True),
    nn.Conv2d(512, 512, kernel_size=3, padding=1),
    nn.ReLU(True),
    nn.MaxPool2d(kernel_size=2, stride=2),
    nn.Conv2d(512, 512, kernel_size=3, padding=1),
    nn.ReLU(True),
    nn.Conv2d(512, 512, kernel_size=3, padding=1),
    nn.ReLU(True),
    nn.Conv2d(512, 512, kernel_size=3, padding=1),
    nn.ReLU(True),
    nn.MaxPool2d(kernel_size=2, stride=2),
    )

# VGG
class VGG(nn.Module):
    def __init__(self, features, num_classes=1000, init_weights=True):
        super(VGG, self).__init__()
        self.features = features
        self.avgpool = nn.AdaptiveAvgPool2d((7, 7))
        self.classifier = nn.Sequential(
        nn.Linear(512 * 7 * 7, 4096),
        nn.ReLU(True),
        nn.Dropout(),
        nn.Linear(4096, 4096),
        nn.ReLU(True),
        nn.Dropout(),
        nn.Linear(4096, num_classes),
        )

    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x
 
# 实例化 VGG 模型并打印
model = VGG(features)
print(model)