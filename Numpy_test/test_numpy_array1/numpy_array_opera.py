# -*- coding:utf-8 -*-

import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(4)
print (a, b)

c = a - b
print c

d = a**2
print d

e = 10*np.sin(a)
print e

# 返回True和false列表
print (b < 3)
print (b == 3)

# 矩阵的乘法
a1 = np.array([[1, 2],
               [3, 4]])
a2 = np.array([[1, 2],
               [3, 4]])
# 普通乘法,对应位逐个相乘
a3 = a1 * a2
# 矩阵乘法
a4 = np.dot(a1, a2)
a5 = a1.dot(a2)

print a3, a4, a5

# 随机数字
r = np.random.random((2, 4))
print np.sum(r)
print np.min(r)
print np.max(r)
# 某一行最大值 axis维度 =1 在行数中  axis = 0 在列中求
print np.sum(r, axis=1)
print np.sum(r, axis=0)
print np.min(r, axis=0)
print np.max(r, axis=1)


