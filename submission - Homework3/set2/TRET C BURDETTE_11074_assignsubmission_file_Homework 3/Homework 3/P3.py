# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:10:39 2016

@author: Tret Burdette
"""

numbers=[3,5,2.3,5,10,4.2]
def minmaxave(numbers):
    return "minimum=", min(numbers), "maximum=", max(numbers), "average=", float(sum(numbers)/len(numbers))

print minmaxave(numbers)