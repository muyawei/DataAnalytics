# -*- coding: utf-8 -*-
import requests

# GET
# /
# {
# 'Connection': 'keep-alive', '
# Accept-Encoding': 'gzip, deflate',
# 'Accept': '*/*',
# 'User-Agent': 'python-requests/2.12.1'
# }
# None
s = requests.get("http://www.12306.cn")
print s.request.method             #返回get，相当于浏览器输入http://www.12306.cn，浏览器不输入get因为浏览器默认为get请求
print s.request.path_url
print s.request.headers
print s.request.body

# GET
s1 = requests.post("http://www.12306.cn")
print s.request.method             #返回get，因为post请求数据时，百度认为是错误的数据，自动重定向到新的网址

# POST
# /
# {
# 'Connection': 'keep-alive',
# 'Content-Length': '0',
# 'Accept-Encoding': 'gzip, deflate',
# 'Accept': '*/*',
# 'User-Agent': 'python-requests/2.12.1'
# }
# None
# 比get多了一个'Content-Length': '0'
s2 = requests.post("http://www.12306.cn", allow_redirects=False)
print s2.request.method
print s2.request.path_url
print s2.request.headers
print s2.request.body
