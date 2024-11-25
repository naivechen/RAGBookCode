import torch
# 定义一个张量并标记需要计算梯度
x = torch.tensor(2.0, requires_grad=True)
# 定义一个函数 y = x^2
y = x ** 2
# 计算 y 相对于 x 的梯度
y.backward()
# 输出梯度值
print(x.grad)