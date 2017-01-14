import numpy as np

a = np.arange(2, 14).reshape((3, 4))
print a

# 返回最小值的索引
print np.argmin(a)
print np.argmax(a)
# 返回平均值　
print np.mean(a)
print np.average(a)
print a.mean()

# 中位数
print np.median(a)

# 逐步加进去 返回12个值
np.cumsum(a)

#累差 若3行4列。返回3行3列
print np.diff(a)

print np.nonzero(a)

print np.sort(a)

# 矩阵的反转 下标索引10 变 01
print np.transpose(a)
print a.T

# 所有小于5的数都变成5，大于9的变成9，其余数保持不变
np.clip(a, 5, 9)
