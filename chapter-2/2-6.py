import torch
# 创建全 0 张量
zeros_tensor = torch.zeros(2, 3)
# 创建全 1 张量
ones_tensor = torch.ones(3, 2)
# 创建指定范围的均匀分布张量
uniform_tensor = torch.rand(2, 2)
# 创建指定范围的正态分布张量
normal_tensor = torch.randn(3, 3)
print(zeros_tensor)
print(ones_tensor)
print(uniform_tensor)
print(normal_tensor)