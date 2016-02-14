# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print "Question 1"
L1={2,3,4,10}
L2={5,3,4,9,10,15}
print "intersections=", L1&L2
print "L1 or L2, but not both=", L1^L2
print "in L1 not L2=", L1-L2
L3= L1|L2
print L3
L2.add(103)
L2.add(20)
L2.add(34)
print L2

print "Question 2"
t=13
stepsize=2
while t<999:
    variable_sum=t+2
    print variable_sum
    t+=stepsize


print "Question 3"
import random
x=[int(300*random.random()) for i in xrange(300)]
#print x
for y in x:
    if ((y%21==0)):
        print y
