import torch
# 定义一个张量
tensor = torch.tensor([[1., 2., 3.], [4., 5., 6.]])
# 计算张量的最大值
max_value = torch.max(tensor)
print(" 计算张量的最大值 : ", max_value)
# 计算张量在指定维度上的最小值
min_value_dim0, _ = torch.min(tensor, dim=0)
print(" 计算张量在指定维度上的最小值 : ", min_value_dim0)
# 计算张量的均值
mean_value = torch.mean(tensor)
print(" 计算张量的均值 : ", mean_value)
# 计算张量的标准差
std_value = torch.std(tensor)
print(" 计算张量的标准差 : ", std_value)