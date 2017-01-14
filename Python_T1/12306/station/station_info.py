# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
if __name__ == "__main__":
    # 先想页面发送请求，获取页面的全部信息
    s = requests.get("http://www.12306.cn/mormhweb/kyyyz/")

    # 通过BeautifulSoup对页面进行解析
    soup = BeautifulSoup(s.content, "html.parser", from_encoding="utf-8")

    # 查看页面的布局，对所要获取的数据进行观察，提取
    # secTable > tbody > tr:nth-child(1) > td.sec2
    datas = soup.select("#secTable > tbody > tr > td")

    with open("station.txt", "w+") as f:
        for data in datas:
            f.write(data.text.encode('utf-8')+'\n')


