# -*- coiding:utf-8 -*-
import pandas as pd
import numpy as np

dates1 = pd.date_range(start="20170103", end="20170126")
dates2 = pd.date_range(start="20170101", periods=20)
dates3 = pd.date_range(end="20170101", periods=20)
dates4 = pd.date_range(start="20170101", end="20180101", freq="BM")
dates5 = pd.date_range(start="20170101", periods=5, freq="1h30min")

print dates1
print dates2
print dates3
print dates4
print dates5

