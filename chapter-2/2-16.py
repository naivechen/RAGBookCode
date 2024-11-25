import torch
# 创建一个张量
tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 整数索引示例
indices = torch.tensor([0, 2])
selected_rows = tensor[indices]
print(" 整数索引 : ", selected_rows)
# 布尔索引示例
condition = tensor > 5
selected_elements = tensor[condition]
print(" 布尔索引 : ", selected_elements)