# Author: Daniel Harper
# Assignment: Lab 2
# Original Date: 1/28/2016
# Last Updated:  1/28/2016
# Written using Python 3.0
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import *

# Body Section#######################################################
#--------------------------------------------------------------------
# 1. store the following student records into a variable using list of tuples
# "jimmhy"  98   35  56
# "jones"   89   88	98
# "lucy"	  99   90   98
# print out jone's third subject score

tupleList = [("jimmhy",98,35,56),("jones",89,88,98),("lucy",99,90,98)]

print(tupleList[1][3])

#--------------------------------------------------------------------
# 2. create a 3 dimension matrix of  3X3X3 and store it into M3 variable
# the values are
# 1 1 1
# 1 1 1
# 1 1 9
#
# 2 2 2
# 2 8 2
# 2 2 2
#
# print the 8, 9 using the M3 variable with indexes

M3 = [[[1, 1, 1], [1, 1, 1], [1, 1, 9]], [[2, 2, 2], [2, 8, 2], [2, 2, 2]]]
print(M3[1][1][1], M3[0][2][2])

#--------------------------------------------------------------------
# 3. Store student subject score for a student into a variable of dictionary
# jimmy's score
# physics: 58
# math:98
# english:98

dictionary = {"physics":58, "math":98, "english":98}
print(dictionary)

#--------------------------------------------------------------------
# 4. Store temperature of 10 cities into a variable  CityT
# specify your own city names. 

CityT = {"Columbia": 49, "New York": 53, "Miami": 39, "Austin": 47, "Atlanta": 44, "Sacramento": 45, "Columbus": 83, "Phoenix": 103, "Washington": 89, "Tallahassee": 83}

print(CityT)

#END OF PROGRAM------------------------------------------------------