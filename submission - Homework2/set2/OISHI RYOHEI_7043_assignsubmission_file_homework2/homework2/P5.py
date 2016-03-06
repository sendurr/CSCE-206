# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 17:24:55 2016

@author: penchibi
"""
x=input("Enter your x: ")
roots=[-1,1,2]
j=1
for i in range(0,len(roots)):
    j=(x-roots[i])*j
print j
