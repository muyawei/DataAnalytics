# -*-coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 3)
y = 2 * x + 1

plt.figure(num=1, figsize=(8, 5),)
plt.plot(x, y)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 会显示点（x,y）的坐标
plt.scatter(x, y, s=50, color='b')
# 画一条竖直的线，x的坐标都为x0，y的坐标为y0和0
x0 = 1
y0 = 2 * x0 + 1
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)

# 注释
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30), textcoords='offset points',
             fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle='arc3,rad=.2'))

plt.text(0, 3, r'$This\ is\ test.\alpha_t$', fontdict={'size': 16, 'color': 'r'})
plt.show()
