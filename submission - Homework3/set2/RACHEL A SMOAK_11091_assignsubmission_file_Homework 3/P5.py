#Rachel Smoak
#Homework 3
#28 February 2016

#Question 5
import sys
t = float(sys.argv[2]) #define t as third item in list
v0 = float(sys.argv[1]) #define v0 as second item in list
g = 9.81
y = v0*t-0.5*g*t**2
print "Position at v0 = ", v0, "and t = ", t, "is", y