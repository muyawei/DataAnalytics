# -*-coding:utf-8 -*-
import pandas as pd
import numpy as np
print "first:"
s = pd.Series([-999, 22, 33])
s = s.replace(-999, np.NaN)
print s

print "second:"
df = pd.DataFrame({"name": ["vic", "jd", "zxy"], "age": [22, 22, 23]})
print df
d = df.replace({"vic": "myw", 23: "max"})
print d


print "third:"
df = pd.DataFrame({"name": ["vic", "jd", "zxy"], "age": [22, 22, 23]})
print df
d = df.replace(["vic", 23], ["myw", "max"])
print d


