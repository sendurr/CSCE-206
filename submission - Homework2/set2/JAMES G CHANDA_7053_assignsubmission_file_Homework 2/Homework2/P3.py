#We want to generate x coordinates between 1 and 2 with spacing 0.01.
#the coordinates are given by the formula xi=1+ih
#where h=0.01 and i runs over integers 0,1,...,100. compute xi values 
#and store them in a list. Use a for loop and append each new xi value 
#to a list, which is empty intiially

from math import *
x= 1
h = 0.01
xcoordinates =[]

for i in range(0,101):
	xi=i*h
	xcoordinates.append(x+xi)


print xcoordinates