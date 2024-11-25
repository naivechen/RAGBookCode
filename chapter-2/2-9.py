import torch
# 定义两个张量
tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[5, 6], [7, 8]])
# 加法
result_add = tensor1 + tensor2
result_add_func = torch.add(tensor1, tensor2)
print("Python 运算符 : ", result_add)
print("PyTorch 提供的函数 : ", result_add_func)
# 减法
result_sub = tensor1 - tensor2
result_sub_func = torch.sub(tensor1, tensor2)
print("Python 运算符 : ", result_sub)
print("PyTorch 提供的函数 : ", result_sub_func)
# 乘法
result_mul = tensor1 * tensor2
result_mul_func = torch.mul(tensor1, tensor2)
print("Python 运算符 : ", result_mul)
print("PyTorch 提供的函数 : ", result_mul_func)
# 除法
result_div = tensor1 / tensor2
result_div_func = torch.div(tensor1, tensor2)
print("Python 运算符 : ", result_div)
print("PyTorch 提供的函数 : ", result_div_func)