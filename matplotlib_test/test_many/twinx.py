# -*-coding:utf-8-*-
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10, 0.1)
y1 = x**2
y2 = -y1 + 1
y2 = y1 + 1  # try

f, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x, y1, 'r-')
ax2.plot(x, y2, 'b--')

ax1.set_xlabel("x")
ax1.set_ylabel('y')

plt.show()
