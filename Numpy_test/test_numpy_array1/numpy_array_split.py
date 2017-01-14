import numpy as np

A = np.arange(12).shape((3, 4))
# 表示分成2块，axis表示横向或正向
print np.split(A, 2, axis=0)

#不等项的分割
print np.array_split(A, 3, axix=1)
print np.vsplit(A, 3)
print np.hsplit(A, 4)
