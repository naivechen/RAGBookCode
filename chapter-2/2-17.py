import torch
# 创建一个 3x4 的张量
tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("tensor 原始形状 : ", tensor.shape)
# 将张量的形状改变为 2x6 的张量
reshaped_tensor = tensor.view(2, 6)
print("tensor 修改之后的形状 : ", reshaped_tensor.shape)