# -*-coding:utf-8-*-
import matplotlib.pyplot as plt

fig = plt.figure()
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot([0, 1], [0, 1])
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

left, bottom, width, height = 0.2, 0.6, 0.2, 0.2
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot([0, 1], [0, 1])
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title_inside')

plt.axes([0.6, 0.2, 0.2, 0.2])
plt.plot([0, 1], [0, 1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('title_inside2')
plt.show()
