import numpy as np
def hamming_distance(bit_string1, bit_string2):
    # 将二进制串转换为数组
    bit_array1 = np.array(list(bit_string1))
    bit_array2 = np.array(list(bit_string2))

    # 计算汉明距离
    distance = np.sum(bit_array1 != bit_array2)
    return distance
# 定义两个二进制串
bit_string1 = "110010"
bit_string2 = "101101"
# 计算汉明距离
distance = hamming_distance(bit_string1, bit_string2)
print(" 二进制串 1：", bit_string1)
print(" 二进制串 2：", bit_string2)
print(" 汉明距离：", distance)