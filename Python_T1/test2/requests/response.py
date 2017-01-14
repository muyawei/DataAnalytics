# -*- coding: utf-8 -*-
import requests

s = requests.get("http://www.12306.cn")
print s.status_code
print s.headers
print s.encoding
print s.text     #被解码的消息体
print s.content  #未被解码的消息体