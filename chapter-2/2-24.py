import torch
# 定义模型参数
w = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(1.0, requires_grad=True)
# 定义输入数据和真实标签
x = torch.tensor([1.0, 2.0, 3.0])
y_true = torch.tensor([2.0, 4.0, 6.0])
# 定义模型预测输出
y_pred = w * x + b
# 计算均方误差损失
loss = torch.mean((y_true - y_pred) ** 2)
# 反向传播计算梯度
loss.backward()
# 输出参数的梯度值
print(w.grad) 
print(b.grad)