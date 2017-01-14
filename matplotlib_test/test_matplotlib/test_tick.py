# -*-coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 3)
y = 2 * x + 1

plt.figure(num=1, figsize=(8, 5),)
plt.plot(x, y)
plt.xlim(-2, 4)
plt.ylim(-2, 10)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white', edgecolor='none', alpha=0.7))
plt.show()