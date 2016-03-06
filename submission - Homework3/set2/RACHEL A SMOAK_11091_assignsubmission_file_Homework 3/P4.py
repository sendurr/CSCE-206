#Rachel Smoak
#Homework 3
#28 February 2016

#Question 4
import sys
t = float(raw_input("This program evaluated the position of an object at time t (s) and initial velocity v0 (m/s). t=?")) #give info and ask for time input
v0 = float(raw_input("v0=?")) #ask for velocity input
g = 9.81
y = v0*t-0.5*g*t**2
print "Position at v0 = ", v0, "and t = ", t, "is", y