import torch
# 指定数据类型为 32 位浮点数
tensor_float = torch.tensor([1, 2, 3], dtype=torch.float32)
# 将张量存储在 GPU 上
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
tensor_gpu = torch.tensor([1, 2, 3], device=device)
# 要求张量跟踪梯度变化
tensor_grad = torch.tensor([1.1, 2.2, 3.3], requires_grad=True)
print(tensor_float)
print(tensor_gpu)
print(tensor_grad)