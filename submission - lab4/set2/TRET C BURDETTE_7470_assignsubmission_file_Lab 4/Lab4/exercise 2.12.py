# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 17:14:33 2016

@author: Tret Burdette
"""

#for loop
M=range(1,101,1)
print M
for k in M:
    S=1.0/k
    print S


#while loop
k=1
stepsize= 1
while k<101:
    s=(1.0/k)
    print s
    k+=stepsize