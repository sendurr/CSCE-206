# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 10:27:22 2016

@author: penchibi
"""
#Define the matrix
q=[['a','b','c'],['d','e','f'],['g','h']]
#number 1 
print q[0][0]
#number 2
print q[1]
#number 3
print q[2][1]
#number 4
print q[1][0]
#About q[-1][-2]
print q[-1][-2]
print "The reason why we get g by using the program above is that a negative index accesses elements from the end of the matrix and count it backwards."