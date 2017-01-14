# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

a = np.array([0.3, 0.2, 0.9,
              0.7, 0.6, 0.8,
              0.5, 0.2, 0.4]).reshape(3, 3)

plt.imshow(a, interpolation='nearest', cmap='bone', origin='upper')
plt.colorbar()

plt.xticks()
plt.yticks()
plt.show()
