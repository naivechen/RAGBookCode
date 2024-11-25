import torch
# 定义一个张量
tensor1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor2 = torch.tensor([10, 20, 30])
# 执行广播运算
result_broadcast = tensor1 + tensor2
print(" 执行广播运算 : ", result_broadcast)