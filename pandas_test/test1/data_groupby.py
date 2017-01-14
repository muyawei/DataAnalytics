# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8)})

A = ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo']
B = ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three']
for a in A:
    for b in B:

        df.query('A=="a"')
