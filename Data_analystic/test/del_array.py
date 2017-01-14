# coding:utf-8
# 数组的删除，一次删除两个数据时，先删除下标靠后的元素
test_array = [1, 2, 3, 4, 5, 6, 7]
for j in range(len(test_array)):
    for i in range(len(test_array)):
        print i, test_array[i]
    print
    del test_array[i]

# 二维数组的定义（对二维数组的操作经常转化为for）
myList = [([0] * 3) for i in range(4)]
print myList


for i in range(len(myList)):
    for j in range(len(myList[0])):
        myList[i][j] = i * j
print myList

lists = [[] for i in range(4)]
print lists
for i in range(len(myList)):
    for j in range(len(myList[0])):
        lists[i].append(j)
print lists


