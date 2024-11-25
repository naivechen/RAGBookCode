import torch
# 创建一个形状为 (1, 3) 的张量
tensor = torch.tensor([[1, 2, 3]])
print("tensor 原始形状 : ", tensor.shape)
# 移除维度为 1 的维度
squeezed_tensor = tensor.squeeze() # 结果为形状为 (3,) 的张量
print("tensor 修改之后的形状 : ", squeezed_tensor.shape)