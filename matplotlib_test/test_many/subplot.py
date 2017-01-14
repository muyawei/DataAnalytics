# -*-coding:utf-8-*-
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(1, 3, 4)
y = 2 * x
plt.figure()
plt.subplot(2, 2, 1)
plt.plot(x, y)

plt.subplot(2, 2, 2)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 2, 3)
plt.plot(x, y)

plt.subplot(2, 2, 4)
plt.plot(x,y)


plt.figure()
plt.subplot(2, 1, 1)
plt.plot(x, y)

plt.subplot(2, 3, 4)
plt.plot(x, y)

plt.subplot(2, 3, 5)
plt.plot(x, y)

plt.subplot(2, 3, 6)
plt.plot(x, y)

plt.show()
