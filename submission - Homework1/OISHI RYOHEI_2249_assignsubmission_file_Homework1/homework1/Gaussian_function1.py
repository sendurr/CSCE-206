# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 10:16:06 2016

@author: penchibi
"""
#import math function
from math import*
#define three variables
m=0
s=2.0
x=1
#calculate the result 
f=(1/sqrt(2*pi*s**2))*exp(-0.5*((x-m)/s)**2)
print f 
print"The result was same as the hand calculator."