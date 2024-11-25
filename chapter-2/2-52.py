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
# 保存整个模型
torch.save(model, 'entire_model.pth')

# 加载整个模型
loaded_model = torch.load('entire_model.pth')
print(loaded_model)