# -*- coding: utf-8 -*-
import requests

# 附加请求正文
#{'Connection': 'keep-alive',
# 'Content-Length': '5',
# 'Accept-Encoding': 'gzip, deflate',
# 'Accept': '*/*',
# 'User-Agent': 'python-requests/2.12.1'}
#hello
data = "hello"
s = requests.get("http://www.12306.cn", data=data)

print s.request.headers
print s.request.body

