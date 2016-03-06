# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:04:54 2016

@author: Tret Burdette
"""

numbers=[2,5,7,4,8,3,5]

sumoddnumber=0
for x in numbers:
    if x%2!=0:
        sumoddnumber+=x
print "sum of odds=", sumoddnumber
