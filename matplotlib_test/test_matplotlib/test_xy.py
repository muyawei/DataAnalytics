# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-1, 1, 20)
y1 = 2*x+1
y2 = x**2

# 一个figure中可以有多个图形，每个线段可以定义颜色，样式和宽度
plt.figure(num=2)
l1, = plt.plot(x, y2, label='one')
l2, = plt.plot(x, y1, color="red", linewidth=1.0, linestyle='--', label='two')
# 取值范围
plt.xlim((-1, 2))
plt.ylim((-1, 2))
# 坐标名称
plt.xlabel("x")
plt.ylabel("y")
# 换刻度　
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1, 2],
           ["bad", "good", "best"]
           )
# 更好看一点的字体(\alpha--数学符号)
plt.yticks([-2, -1, 2],
           [r"$really\ bad$", r"$good\alpha$", r"$best$"]
           )

# 更改坐标轴的位置
# gca = get current axis

ax = plt.gca()  # 即四个边框
ax.spines['right'].set_color("none")  # 去掉两个边框
ax.spines['top'].set_color("none")

ax.xaxis.set_ticks_position('bottom')  # 设置x,y的坐标
ax.yaxis.set_ticks_position('left')
# 相当于设置坐标原点
ax.spines['bottom'].set_position(('data', 0))  # 设置x轴绑定y轴的位置
ax.spines['left'].set_position(('data', 0))  # 设置x轴绑定y轴的位置

# 图例  loc放图例的位置
plt.legend(handles=[l1, l2], labels=['y1', 'y2'], loc='best')

plt.show()

