# -*- coding: utf-8 -*-
import requests

s = requests.get("http://www.baidu.com/s?wd='麦子学院'")
print s.request.url