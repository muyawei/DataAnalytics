# -*- coding:utf-8 -*-
import numpy as np

#定义数组类型
a = np.array([[2, 3],
              [3, 4, 5]])

print a   # a下面没，
print a.ndim
print a.shape
print a.size
print a.dtype

b = np.array([1, 2, 3], dtype=np.int)  # 可以写位数

c = np.zeros((3, 4))  # 定义全部位0的数列

d = np.ones((3, 4), dtype=np.float)

e = np.empty((2, 3))

f = np.arange(0, 10, 2)

g = np.arange(12)

h = np.arange(12).reshape((3, 4))

# 生成一个线段(1开始，10结尾，分成20段，会自动给你分组每个元素的大小)
i = np.linspcae(1, 10, 20)

j = np.linspcae(1, 10, 5).reshape(2, 3)

