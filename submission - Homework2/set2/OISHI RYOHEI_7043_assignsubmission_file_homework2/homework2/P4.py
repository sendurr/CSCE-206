# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 17:16:04 2016

@author: penchibi
"""

a=[1,3,5,7,11]
b=[13,17]
c=a+b
print c
print "numbers in a and b will be printed"
b[0]=-1
d=[e+1 for e in a]
print d 
print" The four numbers in a will be plused by 1 and printed"
d.append(b[0]+1)
d.append(b[-1]+1)
print d[-2:]
print "the last two number,which are the same number added throught the above two operation, will be printed"