1 客运站具体信息在页面没有显示，有两种可能：
  1） 一开始就有信息，html页面被隐藏
  2） 根据用户的操作，进行http请求，获取数据，html数据部分动态更新（请求的url在原网页）
  通过开发者工具，点击按钮，查看network，看是否有请求


2 url编码
  非特殊字符 wd='abc'
  对于特殊字符 将其转化为16进制，并在前面加上%   如 & ====》wd=%26
     中文字符，没个字节转化为16进制，并用%分割  如  https://www.baidu.com/s?wd='中文'=====》https://www.baidu.com/s?wd=%E4%B8%AD%E6%96%87


  requests 库自动对url进行编码
# -*- coding: utf-8 -*-
import requests

s = requests.get("http://www.baidu.com/s?wd='麦子学院'")
print s.request.url

#结果
http://www.baidu.com/s?wd='%E9%BA%A6%E5%AD%90%E5%AD%A6%E9%99%A2'
