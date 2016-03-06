# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 21:20:43 2016

@author: Tret Burdette
"""

a=[1,3,5,7,11]
b=[13,17]
c=a+b
print c   #list a and b are combined in list c
b[0]=-1
d=[e+1 for e in a]
print d   #list d is list a+1 on each element
d.append(b[0]+1)
d.append(b[-1]+1)
print d[-2:]   #prints the last 2 items in list d
