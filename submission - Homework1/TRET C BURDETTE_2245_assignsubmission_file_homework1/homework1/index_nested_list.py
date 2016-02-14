# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 17:18:10 2016

@author: Tret Burdette
"""

q=[['a','b','c'],['d','e','f'],['g','h']]

print q[0][0]
print q[1]
print q[2][1]
print q[1][0]
print q[-1][-2]
#q[-1][-2] gives the value g because the first element in each list is represented by [0] so instead of going from left to right like when using positive numbers in the list selection, using negative numbers works backwards
#going negative goes from bottom to top and right to left 