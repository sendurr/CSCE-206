#Rachel Smoak
#HW1 Question 5

from math import *

x=set([1,3,8,10,14,10,20,25])
y=set([3,3,8,10,15,20,33,55,88])

intersection = x&y
union = x|y
subtract1 = x-y
subtract2 = y-x

print 'Intersection'
print intersection
print
print 'Union'
print union
print
print 'X-Y'
print subtract1
print
print 'Y-X'
print subtract2
