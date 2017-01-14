# -*- coding:utf-8 -*-

"""计算相似度有两种方式：1。欧几里德距离   2。皮尔逊相关度"""
"""计算欧几里德距离"""
"""通过用户距离的累加和判断用户的相似程度"""
# 获取到数据
critics = {
    'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                  'Just My Luck': 3.0, 'Superman Returns': 3.5,
                  'You, Me and Dupree': 2.5,
                  'The Night Listener': 3.0},

    'Gene Seymour': {'Lady in the Water': 3.0,
                     'Snakes on a Plane': 3.5,
                     'Just My Luck': 1.5, 'Superman Returns': 5.0,
                     'The Night Listener': 3.0,
                     'You, Me and Dupree': 3.5},

    'Michael Phillips': {'Lady in the Water': 2.5,
                         'Snakes on a Plane': 3.0,
                         'Superman Returns': 3.5,
                         'The Night Listener': 4.0},

    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                     'The Night Listener': 4.5,
                     'Superman Returns': 4.0,
                     'You, Me and Dupree': 2.5},

    'Mick LaSalle': {'Lady in the Water': 3.0,
                     'Snakes on a Plane': 4.0,
                     'Just My Luck': 2.0, 'Superman Returns': 3.0,
                     'The Night Listener': 3.0,
                     'You, Me and Dupree': 2.0},

    'Jack Matthews': {'Lady in the Water': 3.0,
                      'Snakes on a Plane': 4.0,
                      'The Night Listener': 3.0,
                      'Superman Returns': 5.0,
                      'You, Me and Dupree': 3.5},

    'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0,
             'Superman Returns': 4.0}}

import math


# 欧几里德算法
def sim_euclid(content, person1, person2):
    # 先查看两个人是否看过同样的电影，若没有，则相似度为0,并将一同看过的电影放在列表里
    shared_film = []
    for film_name in content[person1]:
        if film_name in content[person2]:
            shared_film.append(film_name)
    if len(shared_film) == 0:
        return 0
    # 计算所有差值平方和
    sim = sum([pow((content[person1][film] - content[person2][film]), 2)
               for film in shared_film])
    return 1/(sim+1)


# 皮尔逊相关系数(函数将返回介于1和-1之间的值，值为1时，两个人的相关性最高)
def sim_pearson(content, person1, person2):
    shared_film = []
    for film in content[person1]:
        if film in content[person2]:
            shared_film.append(film)
    count = len(shared_film)
    if count == 0:
        return 0
    # 计算两个人所有电影评分的乘积
    sum_xy = sum([content[person1][film]*content[person2][film]
                  for film in shared_film])

    # 计算一个的评分和
    sum_person1 = sum([content[person1][film] for film in shared_film])
    sum_person2 = sum([content[person2][film] for film in shared_film])

    # 计算一个评分的平方和
    power_person1 = sum([pow(content[person1][film], 2)
                         for film in shared_film])
    power_person2 = sum([pow(content[person2][film], 2)
                         for film in shared_film])

    # 计算皮尔逊相关系数
    t_temp = sum_xy - sum_person1 * sum_person2 / count
    b_temp = math.sqrt((power_person1 - pow(sum_person1, 2)/count) *
                       (power_person2 - pow(sum_person2, 2)/count))
    pearson = t_temp / b_temp
    return pearson


# 获取与其他人与自己的品味相似度
def get_match(critics, person, n=5, similarity=sim_pearson):
    score = [(other, similarity(critics, person, other))
             for other in critics if other != person]
    # 对评分进行排序,最高分在前
    # [{'Toby': 0.9912407071619299}, {'Mick LaSalle': 0.5940885257860044},
    #  {'Michael Phillips': 0.40451991747794525},
    #  {'Jack Matthews': 0.7470178808339965},
    #  {'Gene Seymour': 0.39605901719066977},
    #  {'Claudia Puig': 0.5669467095138396}]
    score = sorted(score, key=lambda score: score[1], reverse=True)
    return score[0:n]


# 获取电影推荐，根据 相似度乘积*评分／相似度的累加和
def get_advice(critics, person, similarity=sim_pearson):
    film_score = {}     # 相似度乘积*评分
    film_sim = {}       # 相似度和
    # 遍历除了自己的所有人，将数据进行累加计算
    for other in critics:
        if other != person:
            sim = similarity(critics, person, other)
        # 如果相似度<0，则它的数据不与参与考虑
            if sim < 0:
                continue
            for film in critics[other]:
                if film not in critics[person] or critics[person][film] == 0:
                    score = sim * critics[other][film]
                    film_score.setdefault(film, 0)
                    film_score[film] += score
                    film_sim.setdefault(film, 0)
                    film_sim[film] += sim
    # 获取其加权值,进行排序
    advice = ((film, score/film_sim[film])
              for film, score in film_score.items())
    advice = sorted(advice, key=lambda advice:advice[1], reverse=True)
    return advice


# 将数据进行转换，获取电影相关
def transform(critics):
    film_critics = {}
    for person in critics:
        for film in critics[person]:
            film_critics.setdefault(film, {})
            film_critics[film][person] = critics[person][film]
    return film_critics


# 由基于用户的协作型过滤转化为基于物品的协作型过滤，不需要每次使用是都进行查询，经常更新即可
def similar_film(crities):
    film_similar = {}
    film_critics = transform(crities)
    for film in film_critics:
        films = get_match(film_critics, film, similarity=sim_euclid)
        film_similar[film] = films
    return film_similar


# 基于物品的协作型过滤为用户推荐电影
def get_advice_by_item(critics, film_similar, person):
    film_socre = {}
    film_sim = {}
    # 遍历该用户评价过的所有电影
    for film, score in critics[person].items():
        # 遍历该电影的相似电影
        for sim_film, sim in film_similar[film]:
            if sim_film in critics[person]:
                continue
            film_socre.setdefault(sim_film, 0)
            film_socre[sim_film] += score * sim
            film_sim.setdefault(sim_film, 0)
            film_sim[sim_film] += sim
    result = ((film, film_socre[film]/film_sim[film]) for film in film_socre)
    result = sorted(result, key=lambda result:result[1], reverse=True)
    return result

if __name__ == "__main__":
    result_euclid = sim_euclid(critics, "Lisa Rose", "Gene Seymour")
    result_pearson = sim_pearson(critics, "Lisa Rose", "Gene Seymour")
    print "根据欧几里德得出的结果:", result_euclid
    print "根据皮尔逊相关系数:",result_pearson
    print get_match(critics, "Lisa Rose")
    print get_advice(critics, "Toby")
    film_critics = transform(critics)
    print film_critics
    print get_advice(film_critics, "Lady in the Water")
    print get_match(film_critics, "Lady in the Water")
    film_similar = similar_film(critics)
    print get_advice_by_item(critics, film_similar, "Toby")








