# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

with open("test.html", "r") as f:
    s = f.read()
#通过一个一个查找，可以找到任意节点，但不能直接找到，要递归



soup = BeautifulSoup(s, "html.parser")
root = soup.contents[0]  #相当于获取soup的子节点
print root   #整个根元素的内容
print type(root) #<class 'bs4.element.Tag'>
print type(root.parent) #<class 'bs4.BeautifulSoup'>

#[u'\n', <head>\n<title>demo</title>\n</head>, u'\n', <body>\n        \u591a\u51fa\u6765\u7684\u6570\u636e\n        <h1>\u6807\u9898</h1>\n<a href="">\u7f51\u9875\u94fe\u63a5</a>\n</body>, u'\n']
print root.contents
print len(root.contents)  #5


head = root.contents[0]
print head.next_sibling  #后兄弟节点

u = head.next_sibling
print u.previous_sibling

