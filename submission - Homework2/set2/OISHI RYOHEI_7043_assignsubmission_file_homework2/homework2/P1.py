# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 17:04:01 2016

@author: penchibi
"""

sum=[0,1]

j=0
for i in range(2,1000):
    j=sum[i-1]+sum[i-2]
    sum.append(j)
print sum