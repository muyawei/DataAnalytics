# coding:utf-8
from math import sqrt
import random

# 获取数据
def get_data(filename):
    lines = [line for line in file(filename)]
    word_names = lines[0].strip().split("\t")[1:]
    title_names = []
    datas = []
    for line in lines[1:]:
        p = line.strip().split('\t')
        title_names.append(p[0])
        datas.append([float(x) for x in p[1:]])
    return word_names, title_names, datas


# 用1.0减去皮尔逊相关度之后的结果，这样做的目的是为了防止让相似度越大的两个元素之间的距离变得更小
def pearson(v1, v2):
    # Simple sums
    sum1 = sum(v1)
    sum2 = sum(v2)

    # Sums of the squares
    sum1Sq = sum([pow(v, 2) for v in v1])
    sum2Sq = sum([pow(v, 2) for v in v2])

    # Sum of the products
    pSum = sum([v1[i] * v2[i] for i in range(len(v1))])

    # Calculate r (Pearson score)
    num = pSum - (sum1 * sum2 / len(v1))
    den = sqrt(
        (sum1Sq - pow(sum1, 2) / len(v1)) * (sum2Sq - pow(sum2, 2) / len(v1)))
    if den == 0:
        return 0

    return 1.0 - num / den


# 创建聚类类型
class Bicluster:
    def __init__(self, vec, left=None, right=None, id=None, distance=0.0):
        self.vec = vec
        self.left = left
        self.right = right
        self.id = id
        self.distance = distance


# 分级聚类(每次选出最佳配对形成新聚类，重复下去，直到只剩一个聚类)
def hcluster(rows, distance=pearson):
    distances = {}   # 为了避免重复性的计算，将计算过的距离值（相似度）存放在distance中
    # 将每行数据转化为一个聚类
    clusters = [Bicluster(rows[i], id=i) for i in range(len(rows))]
    current_id = -1  # 记录层级
    while len(clusters) > 1:
        # 最小值
        lowestpair = (0, 1)
        closest = distance(clusters[0].vec, clusters[1].vec)

        # 选出距离最小的两个聚类
        for i in range(len(clusters)):
            for j in range(i+1, len(clusters)):
                if (clusters[i].id, clusters[j].id) not in distances:
                    distances[(clusters[i].id, clusters[j].id)] = \
                        distance(clusters[i].vec, clusters[j].vec)

                _distance = distances[(clusters[i].id, clusters[j].id)]
                if _distance < closest:
                    closest = _distance
                    lowestpair = (i, j)
       # print lowestpair
        # 求两人聚类的均值，形成新的聚类
        new_vec = [(clusters[lowestpair[0]].vec[i] +
                    clusters[lowestpair[1]].vec[i]) / 2.0
                   for i in range(len(clusters[0].vec))]
        new_cluster = Bicluster(vec=new_vec, left=clusters[lowestpair[0]],
                                right=clusters[lowestpair[1]], id=current_id,
                                distance=closest)

        # 最后的整理，current_id -1,删除被合并的两个聚类，添加新的聚类
        current_id -= 1
        #  注意删除的顺序，因为lowestpair的第一个元素一定比第二个元素小，
        #  所以删除第二元素，不会对第一个元素下标有影响
        #  若先删除第一个，可能会出现数组越界的情况
        del clusters[lowestpair[1]]
        del clusters[lowestpair[0]]
        clusters.append(new_cluster)
    return clusters[0]


# 列聚类（对单词进行分析，看哪几个单词的相关性高）--最简单的方法，就是将数据的行，列相互转换
def transform(datas):
    # new_data = [([0]*len(datas)) for i in range(len(datas[0]))]
    # print new_data
    # for i in range(len(datas[0])):
    #     for j in range(len(datas)):
    #         new_data[i][j] = datas[j][i]

    newdata = []
    for i in range(len(datas[0])):
        newrow = [datas[j][i] for j in range(len(datas))]
        newdata.append(newrow)

    return newdata


# k-均值聚类： 预先告诉算法希望生成的聚类数量，然后算法会根据数据的结构状况来确定聚类的大小
# 分级聚类的缺点： 该算法的计算量非常惊人
# 首先会随机确定K个中心位置，然后将各个数据项分配给最临近的中心点。
# 待分配完成之后，聚类中心就会移到分配给该聚类的所有节点的平均位置处。
# 然后整个分配过程重新开始。这个过程会一直重复下去，直到分配过程不再产生变化为止。

def k_cluster(datas, distance=pearson, k=4):
    # 获取每一列数据的最大值和最小值，
    ranges = [(min([row[i]for row in datas]), max([row[i]for row in datas]))
              for i in range(len(datas[0]))]
    a = [0.8, 0.7, 0.6, 0.5]
    # 随机确定k个中心位置（在所有数据的范围内）
    # clusters = [[random.random() * (ranges[j][1]-ranges[j][0]) + ranges[j][0]
    #             for j in range(len(datas[0]))] for i in range(k)]
    clusters = [
        [a[i] * (ranges[j][1] - ranges[j][0]) + ranges[j][0]
         for j in range(len(datas[0]))] for i in range(k)]
    last_matcher = None
    for n in range(100):
        print n

        # 遍历最所有的项与k的距离，将最小的纳入k中
        best_matcher = [[] for i in range(k)]   # 定义一个二维的数组，[聚类id][row_ids]
        for j in range(len(datas)):
            # 默认将第0个中心位置是最近的
            row = datas[j]
            best_cluster = 0
            for i in range(k):
                d = distance(row, clusters[i])
                if d < distance(row, clusters[best_cluster]):
                    best_cluster = i
            best_matcher[best_cluster].append(j)

        if best_matcher == last_matcher:
            break
        last_matcher = best_matcher

        # 聚类中心就会移到分配给该聚类的所有节点的平均位置处
        for i in range(k):
            avg = [0.0] * len(datas[0])
            if len(best_matcher[i]) > 0:
                for row_id in best_matcher[i]:
                    for m in range(len(datas[row_id])):
                        avg[m] += datas[row_id][m]
                for j in range(len(avg)):
                    avg[j] /= len(best_matcher[i])
                clusters[i] = avg
    print best_matcher
    return best_matcher




if __name__ == "__main__":
    words, titles, datas = get_data("blogdata.txt")
   # print hcluster(datas)
   # print transform(datas)
    print k_cluster(datas) 