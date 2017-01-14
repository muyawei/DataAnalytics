# -*-coding:utf-8-*-
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
# 通过索引的方式进行
plt.figure()
gs = gridspec.GridSpec(3, 3)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1, :2])
ax3 = plt.subplot(gs[1:, 2])
ax4 = plt.subplot(gs[-1, 0])
ax5 = plt.subplot(gs[2, 1])

plt.show()