# -*- coding: utf-8 -*-
import requests
# 附加headerß
#{
# 'a': '1', 'b': '2',
# 'Accept-Encoding': 'gzip, deflate',
# 'Accept': '*/*',
# 'User-Agent': 'python-requests/2.12.1',
# 'Connection': 'keep-alive'
# }
headers = {"a": "1", "b": "2"}
s = requests.get("http://www.12306.cn", headers=headers)

print s.request.method
print s.request.path_url
print s.request.headers

