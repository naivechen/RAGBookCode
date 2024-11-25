
import numpy as np
import torch
# 加载外部数据集
data = np.load('data.npy')
# 转换为 PyTorch 张量
tensor_data = torch.tensor(data)
print(tensor_data.shape)  # 输出张量形状
