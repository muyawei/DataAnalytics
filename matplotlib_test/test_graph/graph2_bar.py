# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1 - X/float(n))
Y2 = (1 - X/float(n))

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2)

for x, y in zip(X, Y1):
    plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center',va='bottom')

for x, y in zip(X, Y2):
    plt.text(x+0.4, -y-0.05, '%.2f' % y, ha='center', va='top')

plt.show()