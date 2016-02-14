# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 10:07:08 2016

@author: penchibi
"""
#define the variables
p=5
A=1000.0
n=3
#Define the function
def money(A,n):
    return A*(1+p/100.0)**n
#print out the result
print money(A,n)
