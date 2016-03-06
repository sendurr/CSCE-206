# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 16:48:31 2016

@author: penchibi
"""
#I could not understand the statement" Use n uniformaly spaced t values throughout the interval[0,2v0/g]
#Therefore I set a range from 0 to 2.0*v0/g and the step to have eleven values(n)
v0=1
g=9.81
n=11

def y(t):
    return v0*t-0.5*g*t**2
t=0
while t < 2.0*v0/g:
    print t,'\t',y(t)
    t+=0.02
    