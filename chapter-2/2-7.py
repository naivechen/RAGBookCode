import torch
# 指定数据类型和设备
tensor = torch.zeros(2, 2, dtype=torch.float32, device='cpu')
print(tensor)
# 要求张量跟踪梯度变化
tensor = torch.ones(2, 2, requires_grad=True)
print(tensor)