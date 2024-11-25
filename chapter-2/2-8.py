import torch
# 从现有张量创建形状相同的新张量
tensor1 = torch.zeros(2, 3)
tensor2 = torch.empty_like(tensor1) # 创建与 tensor1 形状相同的全 0 张量
# 从现有张量创建形状相同但值不同的新张量
tensor3 = torch.ones_like(tensor1) # 创建与 tensor1 形状相同的全 1 张量
print(tensor1)
print(tensor2)
print(tensor3)