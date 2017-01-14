# -*- coding:utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup


# 客运站数据（车站）
# mainTable > tbody:nth-child(1) > tr > td > table > tbody > tr > td:nth-child(1) > table > tbody > tr > td.submenu_bg > a
# 客运站数据 （乘降所）
# mainTable > tbody:nth-child(1) > tr > td > table > tbody > tr > td:nth-child(3) > table > tbody > tr > td.submenu_bg > a
#为每个车站和乘降所建立一个文件
def getDatas(url):
    print url
    det_s = requests.get(url)
    det_soup = BeautifulSoup(det_s.content, "html.parser", from_encoding="utf-8")
    # body > table > tbody > tr > td > div > table > tbody > tr:nth-child(1) > th:nth-child(1)
    datas = det_soup.select("table table tr")
    # if len(datas) <= 2:
    #     print "find nothing"
    out = ''
    for i in range(0, len(datas)):
        if i < 2:
            continue
        infos = datas[i].find_all("td")
        # print infos
        for info in infos:
            out += info.text.encode('utf-8') + '\t'
        out += '\n'
        # print info.text.encode('utf-8') + '\n'
    return out


def output_info(name, url1, url2):
    for x in range(0, len(name)):
        with open(name[x].text.encode('utf-8') + u"(车站).txt".encode('utf-8'), "w+") as f1:
            data1 = getDatas(url1[x])
            f1.write(data1)

        with open(name[x].text.encode('utf-8') + u"(乘降所).txt".encode('utf-8'), "w+") as f2:
            data2 = getDatas(url2[x])
            f2.write(data2)



if __name__ == "__main__":
    page_url = "http://www.12306.cn/mormhweb/kyyyz/"
    s = requests.get(page_url)
    soup = BeautifulSoup(s.content, "html.parser", from_encoding="utf-8")
    # print soup
    #获取所有的url
    urls = soup.select("#mainTable td.submenu_bg > a")
    # print urls
    names = soup.select("#secTable > tbody > tr > td")
    # print names
    all_url1 = [] #车站
    all_url2 = [] #乘降所
    for i in range(0, len(names)):
        all_url1.append(page_url + urls[2 * i]['href'])
        all_url2.append(page_url + urls[2 * i + 1]['href'])
    print all_url1, all_url2
    output_info(names, all_url1, all_url2)









