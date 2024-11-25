import torch
# 从 Python 列表创建张量
tensor1 = torch.tensor([1, 2, 3, 4])
# 从元组创建张量
tensor2 = torch.tensor((5, 6, 7, 8))
# 从 NumPy 数组创建张量
import numpy as np
numpy_array = np.array([9, 10, 11, 12])
tensor3 = torch.tensor(numpy_array)
print(tensor1)
print(tensor2)
print(tensor3)