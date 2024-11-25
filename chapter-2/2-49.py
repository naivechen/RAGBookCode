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
# 保存模型参数
torch.save(model.state_dict(), 'model_params.pth')
