import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

C = np.vstack((A, B))
print C
print A.shape, C.shape

D = np.hstack((A, B))
print D
print A.shape, D.shape

# 不能一维的进行反转
print A.T
# 在行上加了一个维度
print A[np.newaxis, :].shape
# 在列上面加了一个维度
print A[:, np.newaxis].shape

A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]
C = np.vstack((A, B))
print C
print A.shape, C.shape

D = np.hstack((A, B))
print D
print A.shape, D.shape


#多个进行合并
C = np.concatenate((A, B, B, A), axis=1)
print C

C = np.concatenate((A, B, B, A), axis=0)
print C

