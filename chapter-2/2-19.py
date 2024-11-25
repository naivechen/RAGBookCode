import torch
# 创建一个 3x4 的张量
tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("tensor 原始形状 : ", tensor.shape)
# 对张量进行转置操作
transposed_tensor = tensor.transpose(0, 1) # 将张量的行列交换
print("tensor 修改之后的形状 : ", transposed_tensor.shape)