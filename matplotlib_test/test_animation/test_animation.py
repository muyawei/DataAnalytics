# -*-coding:utf-8-*-
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def ts_animation(i):
    line.set_ydata(np.sin(x+i/100))
    return line,


def im():
    line.set_ydata(np.sin(x))
    return line,


# 变化的更新，还是全部更新 blit
ani = animation.FuncAnimation(fig=fig, func=ts_animation, frams=100, init_func=im, interval=20, blit=False)
plt.show()
