# -*-coding:utf-8-*-
import matplotlib.pyplot as plt

# f指返回的figure，对figure的设置，直接修改f即可
f, ((ax11, ax22), (ax33, ax44)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.plot([0, 1], [0, 1])

plt.tight_layout()
plt.show()