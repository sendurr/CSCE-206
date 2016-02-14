# question 1
x = 2.33
print "x=", x

y = -2
print "y=", y

z= 32233
print "z=", z

a= "I am a boy"
print "a=", a

# question 2
array1= [3, 4.0, 34, -5, 23]
evenslist = [x for x in array1 if x % 2 == 0]
print evenslist

feedback = ["good","very good","excellent"]
print feedback[0]
print feedback[-1]

from numpy import matrix
from numpy import linalg
M = matrix([[1,2,3],[4,5,6],[7,8,9]])
print M
print M.item(4)
