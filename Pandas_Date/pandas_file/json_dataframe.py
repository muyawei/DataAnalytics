# coding:utf-8
import pandas as pd
import json

# json.loads将json转化为python对象
j = """{"name": "vic", "age": 22, "friends": [{"name": "jd", "age": "22"}, {"name": "wyh", "age": "22"}]}"""
data = json.loads(j)
print data

# 将python对象转化为json
j = json.dumps(data)
print j

print pd.DataFrame(data)
print pd.DataFrame(data["friends"])



