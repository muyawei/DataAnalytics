# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
#使用find进行查找　
with open("test.html", "r") as f:
    s = f.read()

soup = BeautifulSoup(s, "html.parser")
print soup.find("a")
print soup.find("b", attrs={"href": ""})

#print soup.find("path").find(attrs={"start":"1"})find_all("li")[2]



#使用select进行查找，即css选择器
print soup.select("a") #根据元素名称
print soup.select("[href:]") #根据属性
print soup.select("a[href:]") #元素和属性联合


#级联查找
print soup.select("body ol li")

print soup.select("body ol:nth-of-type(1) li:nth-of-type(2)")  #从1开始进行



