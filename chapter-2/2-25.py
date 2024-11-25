import torch
# 定义模型参数
w = torch.tensor(3.0, requires_grad=True)
b = torch.tensor(1.0, requires_grad=True)
# 定义输入数据和真实标签
x = torch.tensor([2.0])
y_true = torch.tensor([7.0])
# 假设这是一个简单的模型预测过程
y_pred = w * x + b
# 计算均方误差损失
loss = torch.mean((y_true - y_pred) ** 2)
# 停止梯度传播，固定参数
with torch.no_grad():
    w += 1.0 # w 参数不再更新
    b += 0.5 # b 参数不再更新
    # 输出固定后的参数
    print(w) 
    print(b)