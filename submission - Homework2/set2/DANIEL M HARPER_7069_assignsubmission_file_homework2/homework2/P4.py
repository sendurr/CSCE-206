# Author: Daniel Harper
# Assignment: Homework 2 - P4.py
# Original Date: 2/4/2016
# Last Updated:  2/4/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import *
#import random

# Body Section#######################################################
#--------------------------------------------------------------------
# Simulate operations on lists by hand. You are given the following 
# program:
# a = [1, 3, 5, 7, 11]
# b = [13, 17]
# c = a + b
# print c
# b[0] = -1
# d = [e+1 for e in a]
# print d
# d.append(b[0] + 1)
# d.append(b[-1] + 1)
# print d[-2:]
#####################################################################
# print c will print [1, 3, 5, 7, 13, 17]. This is because the + 
#     operator is the concatenation operator. The concatenation of a
#     and b is a single list of the above elements

# print d will print [2, 4, 6, 8, 12]. This is because d starts as a 
#     copy of a, but then the for loop in the d constructor
#     increases each element by 1. The resulting list is above

# print d[-2:] will print [0, 18]. This is because d starts as a 
#     copy. Then all of d's elements are increment +1. Then d is
#     appended with the first and last elements of b incremented by 1
#     The list d results in [2, 3, 6, 8, 12, 0, 18]