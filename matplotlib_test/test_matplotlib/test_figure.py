# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 20)
y1 = 2*x+1
y2 = x**2

# 每个figure开头都是一个范围的开始
plt.figure(num=1, figsize=(8, 5))
plt.plot(x, y1)

# 一个figure中可以有多个图形，每个线段可以定义颜色，样式和宽度
plt.figure(num=2)
plt.plot(x, y2)
plt.plot(x, y1, color="red", linewidth=1.0, linestyle='--')
plt.show()
