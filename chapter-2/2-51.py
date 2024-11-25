import torch
import torch.nn as nn
# 定义一个简单的神经网络模型
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 5)

    def forward(self, x):
        return self.fc(x)
    
# 创建模型实例
model = SimpleModel()
# 加载模型参数
model.load_state_dict(torch.load('model_params.pth'))
print(model)