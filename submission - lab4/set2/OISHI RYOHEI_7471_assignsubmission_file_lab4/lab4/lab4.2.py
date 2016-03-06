# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 22:16:17 2016

@author: penchibi
"""
k=0
sum=0
M=input("Please enter how many times you wanto to repeat the summation: ")
for k in range(1,M+1):
    sum=sum+1/float(k)
print sum

M1=input("Please enter how many times you want to repeat the summation, again: ")
k1=1
sum1=0
while k1<M1+1:
    sum1=sum1+1/float(k1)
    k1=k1+1
print sum1