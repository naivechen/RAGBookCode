import torch
# 创建一个张量
tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 修改张量中的元素
tensor[0, 1] = 10 # 将第一行第二列的元素修改为 10
print(" 修改单个元素 : ", tensor)
# 使用切片修改张量中的子张量
tensor[:, 1:3] = 0 # 将所有行的第二列到第三列的元素修改为 0
print(" 修改切片元素 : ", tensor)