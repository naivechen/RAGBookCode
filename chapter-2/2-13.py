import torch
# 创建一个张量
tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 访问张量中的单个元素
element = tensor[1, 2] # 获取第二行第三列的元素，值为 6
print(" 访问张量中的元素 : ", element)