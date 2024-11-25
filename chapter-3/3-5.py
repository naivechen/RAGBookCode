import torch
import torch.nn as nn
# 定义卷积层
class ConvolutionalLayer(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride, padding):
        super(ConvolutionalLayer, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding)

    def forward(self, x):
        out = self.conv(x)
        return out

# 准备数据
batch_size = 1
in_channels = 3 # 输入数据的通道数（RGB 图像通道数为 3）
input_height = 32 # 输入数据的高度
input_width = 32 # 输入数据的宽度
input_data = torch.randn(batch_size, in_channels, input_height, input_width) # 输入数据

# 创建卷积层
out_channels = 16 # 输出通道数
kernel_size = 3 # 卷积核大小
stride = 1 # 步长
padding = 1 # 填充
conv_layer = ConvolutionalLayer(in_channels, out_channels, kernel_size, stride, padding)
# 前向传播
output_data = conv_layer(input_data)




# 定义池化层
class MaxPoolingLayer(nn.Module):
    def __init__(self, kernel_size, stride):
        super(MaxPoolingLayer, self).__init__()
        self.pool = nn.MaxPool2d(kernel_size, stride)

    def forward(self, x):
        out = self.pool(x)
        return out
    
# 创建池化层
kernel_size = 2 # 池化核大小
stride = 2 # 步长
pool_layer = MaxPoolingLayer(kernel_size, stride)
# 前向传播
output_data = pool_layer(output_data)
print("Output shape after max pooling:", output_data.shape)