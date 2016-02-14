# Author: Daniel Harper
# Assignment: Homework 1 - setFunctions.py
# Original Date: 1/21/2016
# Last Updated:  1/21/2016
# Written using Python 3.4.3.7
# All rights reserved
# Description: Accomplish tasks outlined in the assignment document
#####################################################################
# Importation Section################################################
#from math import * # basic math library

# Body Section#######################################################

#X = set([1,2,8,10,20,25])
X = {1,2,8,10,20,25}

#Y = set([3,3,8,10,15,20,33,55,88])
Y = {3,3,8,10,15,20,33,55,88}

#print(X)

#print(Y)

#print(set.intersection(X,Y))
print(X & Y)

#print(set.union(X,Y))
print(X | Y)

#print(set(X-Y))
print(X - Y)

#print(set(Y-X))
print(Y - X)