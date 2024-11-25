import torch
# 创建一个张量
tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 切片操作示例
slice_tensor = tensor[0:2, 1:3] # 获取第一行到第二行、第二列到第三列的子张量
print(" 切片输出结果为 : ", slice_tensor)