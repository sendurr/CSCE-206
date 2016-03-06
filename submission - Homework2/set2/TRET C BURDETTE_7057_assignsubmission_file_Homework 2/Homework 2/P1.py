# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 20:04:53 2016

@author: Tret Burdette
"""

import sys
sys.setrecursionlimit(1*10^99)
def f(n):
    if n==0: 
        return 0
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)
print f(4) #program can generate the first 1000 terms depending on what is inserted in () 
