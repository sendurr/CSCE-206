# Author: Daniel Harper
# Assignment: Homework 1 - index_nested_list.py
# Original Date: 1/21/2016
# Last Updated:  1/21/2016
# Written using Python 3.4.3.7
# All rights reserved
# Description: Accomplish tasks outlined in the assignment document
#####################################################################
# Importation Section################################################
# from math import * # basic math library

# Body Section#######################################################

# Nested lists outlined by the assignment document
q = [['a','b','c'],['d','e','f'],['g','h']]

# 1) Index the letter a
print(q[0][0])

# 2) Index the list ['d','e','f']
print(q[1])

# 3) Index the last element h
print(q[2][1])

# 4) Index the element d
print(q[1][0])

# 5) Explain why this works this way (it prints g)
print(q[-1][-2])

# EXPLANATION for part 5)--------------------------------------------
# Negative indexs in python allow the programmer to count from the 
# back (right or end) of the list. [0][0] is the reference of the
# first item, and [-1][-1] is the last item in the list. Decreasing 
# the negative integers will count from the back-end of the list. 
# By allowing the programmer to count from the back of the list, 
# programs become more efficient and easier to write.
# -------------------------------------------------------------------