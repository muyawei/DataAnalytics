import numpy as np
a = np.arange(4)
# a的赋给b，b与a关联
b = a
print a is b
a[0] = 11
print a
print b
# a的赋给c，b与a不关联
c = a.copy()
print c is a
a[0] = 22
print a
print c