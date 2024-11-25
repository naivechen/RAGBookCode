import torch
from torch.utils.data import Dataset, DataLoader
class CustomDataset(Dataset):
    def __init__(self, data, targets):
        self.data = data
        self.targets = targets

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        x = self.data[index]
        y = self.targets[index]

        # 处理缺失值
        if torch.isnan(x).any():
            x = torch.zeros_like(x) # 填充为零向量

        return x, y


# 创建示例数据，包括一些带有 NaN 的数据点
data = torch.tensor([[1.0, 2.0], [float('nan'), 3.0], [4.0, 5.0]])
targets = torch.tensor([0, 1, 0])
# 创建数据集
dataset = CustomDataset(data, targets)
# 创建 DataLoader
dataloader = DataLoader(dataset, batch_size=1, shuffle=True)
# 遍历数据
for batch_idx, (x, y) in enumerate(dataloader):
    print(f"Batch {batch_idx}:")
    print("Data:", x)
    print("Target:", y)
