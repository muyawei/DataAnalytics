# -*- coding:utf-8 -*-
import numpy as np

a = np.arange(3, 15)
print a
print a[3]

b = np.arange(3, 15).reshape((3, 4))
print b[2]
print b[1][1]
# 第一行第一个数
print b[1, 1]
# 第一行所有数
print b[1, :]
# 第一列所有数
print b[:, 1]
# 第一行的第1列到第3列的所有数
print b[1, 1:3]

print b
# 输出每一行的数
for row in b:
    print row

# 输出每一列的数(自己实现)---迭代他对称的行就是迭代当前矩阵的列
for row in b.T:
    print row
# 改成一维
print a.flatten()

# 一个一个的输出
for item in a.flat:
    print item
