# -*- coding:utf-8 -*-
from datetime import datetime, timedelta


now = datetime.now()
print now
print now.year
print now.month
print now.day

delta = datetime(2016, 12, 31) - datetime(2016, 04, 01)
print delta
print delta.days
print delta.seconds

print datetime.now() - timedelta(days=1)
print datetime.now().strftime("%Y-%m-%d")

