import torch
# 创建一个形状为 (3,) 的张量
tensor = torch.tensor([1, 2, 3])
print("tensor 原始形状 : ", tensor.shape)
# 在第一个维度位置增加一个维度
unsqueeze_tensor = tensor.unsqueeze(0) # 结果为形状为 (1, 3) 的张量
print("tensor 修改之后的形状 : ", unsqueeze_tensor.shape)