# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 22:24:50 2016

@author: penchibi
"""
sum=0
M=[[1,2,3],[4,5,6],[7,8,9]]
for i in range (0,len(M)):
    for j in range(0,len(M)):
        sum=sum+M[i][j]
print sum