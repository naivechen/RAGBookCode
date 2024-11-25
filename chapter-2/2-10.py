import torch
# 定义两个张量
tensor1 = torch.tensor([[True, False], [False, True]])
tensor2 = torch.tensor([[False, True], [True, False]])
# 逻辑与
result_and = tensor1 & tensor2
result_and_func = torch.logical_and(tensor1, tensor2)
print(" 逻辑与 :", result_and, result_and_func)
# 逻辑或
result_or = tensor1 | tensor2
result_or_func = torch.logical_or(tensor1, tensor2)
print(" 逻辑或 :", result_or, result_or_func)
# 逻辑非
result_not = ~tensor1
result_not_func = torch.logical_not(tensor1)
print(" 逻辑非 :", result_not, result_not_func)