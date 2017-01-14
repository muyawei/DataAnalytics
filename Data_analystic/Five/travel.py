# coding:utf-8

import time
import random
import math
#  选取最优算法，首先构造测试数据
# 人员及其始发地

people = [('Seymour', 'BOS'),
          ('Franny', 'DAL'),
          ('Zooey', 'CAK'),
          ('Walt', 'MIA'),
          ('Buddy', 'ORD'),
          ('Les', 'OMA')]
# Laguardia
destination = 'LGA'

# 从文件中获取航班信息

# 这样操作数据有问题
# with open("schedule.txt") as file:
#     while file.readline() != "":
#         line = file.readline()
fights = {}
# 数据格式{(origin, dest): [(depart, arrival, price), (depart, arrival, price)....]
#         (origin, dest): [(depart, arrival, price), (depart, arrival, price)....]
#        }
for line in open("schedule.txt"):
    origin, dest, depart, arrival, price = line.split(",")
    fights.setdefault((origin, dest), [])
    fights[(origin, dest)].append((depart, arrival, int(price)))
print fights


# 对于时间的处理 文本的时间格式为 10:22
def get_times(_time):
    t = time.strptime(_time, "%H:%M")
    return t[3] * 60 + t[4]


#  得到一组值之后，将数据进行输出
#  若是5个人，则应该有10组数据，每个人的往返
def print_schedule(plan):
    for i in range(len(plan) / 2):
        _people = people[i][0]
        _origin = people[i][1]
        _depart, _arrival, _price = fights[(_origin, dest)][plan[2 * i]]
        depart, arrival, price = fights[(dest, _origin)][plan[2 * i + 1]]
        print '%10s%10s %5s-%5s $%3s %5s-%5s $%3s' % (_people, _origin,
                                                      _depart, _arrival, _price,
                                                      depart, arrival, price)

print_schedule([1, 4, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3])


# 定义成本函数---选取方案的决定性作用
# 我们这里考察 所有航班的价格， 等待时间
def schedule_cost(plan):
    total_cost = 0
    last_arrive = 0   # 到达最晚时间
    earlister_return = 24 * 60  # 最早离开时间
    for i in range(len(plan) / 2):
        origin = people[i][1]
        outbound = fights[(origin, dest)][plan[2 * i]]
        returnhome = fights[(dest, origin)][plan[2 * i + 1]]
        # 所有航班的价格
        total_cost += outbound[2]
        total_cost += returnhome[2]

        # 获取最晚到达，和最早离开时间
        if last_arrive < get_times(outbound[1]):
            last_arrive = get_times(outbound[1])
        if earlister_return > get_times(returnhome[0]):
            earlister_return = get_times(returnhome[0])

    # 获取所有的等待时间
    wait_time = 0
    for i in range(len(plan) / 2):
        origin = people[i][1]
        wait_time += last_arrive - get_times(fights[(origin, dest)][plan[2 * i]][1])
        wait_time += get_times(fights[(dest, origin)][plan[2 * i + 1]][0]) - earlister_return

    return total_cost + wait_time
print schedule_cost([1, 4, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3])


# 对于本数据，一共有12个航班，每个航班又有10中可能，就是10的12次幂。计算次数很多，消耗时间过长
# 最基本的优化方法：随机生成若干组plan，进行比较，选取最优值
# 传入的domain是有航班的最小编号和最大编号组成的列表
def randomoptimize(domain, count=100, schedule_cost=schedule_cost):
    max_cost = 9999999
    best_plan = []
    for cnt in range(0, count):
        rand_plan = [random.randint(domain[i][0], domain[i][1]) for i in range(len(domain))]
        cost = schedule_cost(rand_plan)
        if cost < max_cost:
            max_cost = cost
            best_plan = rand_plan
    return best_plan
domain = [(0, 9)] * 12
print randomoptimize(domain)


#  对于随机算法，得到的结果往往不会很理想，不能充分利用已发现的优解（到处跳跃）
#  利用爬山法解决这个问题----- 随机选取一组解，在这个解上的每个数据进行移动，获取它的邻居，找到最小值。
#                            若最小值就是当前节点，说明它是一个谷底

def hillclimb(domain, schedule_cost=schedule_cost):
    # 获取初始解
    plan = [random.randint(domain[i][0], domain[i][1]) for i in range(len(domain))]
    # plan = [1, 4, 3]
    best_plan = plan
    #  获取它的邻居
    while 1:
        neighbors = []
        for i in range(len(best_plan)):
            if plan[i] > domain[i][0]:
                neighbors.append(plan[0:i]+[plan[i] - 1]+plan[i+1:])
            if plan[i] < domain[i][1]:
                neighbors.append(plan[0:i]+[plan[i] + 1]+plan[i + 1:])
        currnt_cost = schedule_cost(best_plan)
        min_cost = currnt_cost
        for i in range(len(neighbors)):
            print i
            neig_cost = schedule_cost(neighbors[i])
            if neig_cost < min_cost:
                min_cost = neig_cost
                best_plan = neighbors[i]

        if min_cost == currnt_cost:
            break
    return best_plan
domain = [(0, 5)] * 3
print hillclimb(domain)


# 爬山法获取的最小值是局部性的，可能有更低的谷底
# 解决方法，使用退火法  ---- 他允许使用较差的情况替代较好的情况，这样有机会去到更低的谷底
#                           随着温度的变化，他只会接受较差的情况，不会接受极差的情况
# 随机初始化一组值，在温度退到指定位置前，每次随机一个索引和一个step，将数据进行移动，
# 获取较好的或者范围允许的数据
# p = pow(math.e, (-eb - ea) / T)
def annealingoptimize(domain, costf=schedule_cost, T=10000.0, cool=0.95, step=1):
    # 获取随机值
    plan = [random.randint(domain[i][0], domain[i][1])for i in range(len(domain))]
    plan = [1, 4, 3]
    while T > 0.1:
       #  每次随机一个索引和一个step，将数据进行移动
        index = random.randint(0, len(domain) - 1)
        dir = random.randint(-step, +step)
        _plan = plan[:]
        _plan[index] += dir
        if _plan[index] < domain[index][0]:
            _plan[index] = domain[index][0]
        if _plan[index] > domain[index][1]:
            _plan[index] = domain[index][1]
        plan_cost = costf(plan)
        _plan_cost = costf(_plan)
        p = pow(math.e, -(_plan_cost - plan_cost) / T)
        if _plan_cost < plan_cost or random.random < p:
            plan = _plan
        T *= cool
    return plan
domain = [(0, 5)] * 3
print annealingoptimize(domain)


# 另一种解决局部性最小值的办法是遗传算法
# 随机创建一组解作为种群
# 计算种群的成本函数，进行排序。获取其中的前n个解（优质解），作为新种群（用于繁殖下一代）
# 新种群中剩下的成员，由优质解变异或者交叉产生（由随机数进行控制）
#                    --- 变异 ：对于一组解随机选取一个数字，对其进行增减
#                    --- 交叉 ：随机选取一个索引，两组数据以索引进行拼接
# 循环繁殖n代，选出最后结果
# popsize : 种群大小      step: 变异的大小   mutprob：变异还是遗传
# elite：每个种群中前多少为优质  maxiter:繁殖多少代
def geneticoptimize(domain, costf=schedule_cost, popsize=50, step=1,
                    mutprob=0.2, elite=0.4, maxiter=100):
    # 变异
    def mutate(plan):
        index = random.randint(0, len(domain) - step)
        if plan[index] > domain[index][0]:
            return plan[0:index] + [plan[index] - step] + plan[index+1:]
        elif plan[index] < domain[index][1]:
            return plan[0:index] + [plan[index]+1] + plan[index+1:]

    # 交叉
    def crossover(plan_1, plan_2):
        index = random.randint(1, len(domain) - 2)
        return plan_1[0:index] + plan_2[index:]

    # 产生一个群组
    pop = []
    for i in range(popsize):
        pop.append([random.randint(domain[i][0], domain[i][1]) for i in range(len(domain))])

    # 进行maxiter次繁殖
    for i in range(maxiter):
        # 计算成本，进行排序
        ranked_cost_plan = [(costf(plan), plan) for plan in pop]
        ranked_cost_plan.sort()
        ranked_plan = [plan for (cost, plan) in ranked_cost_plan]
        # 取得优质解
        better_size = int(popsize * elite)
        pop = ranked_plan[:better_size]
        # 若种群数量不够，变异或交叉产生
        while len(pop) < popsize:
            if random.random < mutprob:
                # 变异
                rand_plan = pop[random.randint(0, better_size -1)]
                pop.append(mutate(rand_plan))
            else:
                # 交叉
                rand_plan_1 = pop[random.randint(0, better_size - 1)]
                rand_plan_2 = pop[random.randint(0, better_size - 1)]
                pop.append(crossover(rand_plan_1, rand_plan_2))

        print ranked_cost_plan[0][0]
    return pop[0]
domain = [(0, 9)] * 4
print geneticoptimize(domain)

