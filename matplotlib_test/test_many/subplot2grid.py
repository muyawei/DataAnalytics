# -*-coding:utf-8-*-
import matplotlib.pyplot as plt


plt.figure()
# 第一个参数是表格一共分成几行几列，第二个参数是表格的起始位置，第0行第0列，
# 第三个参数是占几列，第四个参数是占几行
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=1)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))

ax1.plot([0, 1], [0, 1])
ax2.plot([0, 1], [0, 1])
ax3.plot([0, 1], [0, 1])
ax4.plot([0, 1], [0, 1])
ax5.plot([0, 1], [0, 1])

plt.show()
