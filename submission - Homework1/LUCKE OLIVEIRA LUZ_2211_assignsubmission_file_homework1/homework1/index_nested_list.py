# Name: Lucke Oliveira Luz   Assignment: Homework 1   Exercise: 2.19

q = [['a','b','c'],['d','e','f'],['g','h']]
print "first element 'a' =", q[0][0]
print "second list =", q[1]
print "last element 'h' =", q[2][1]
print "'d' element =", q[1][0]

#IF WE PRINT q[-1][-2] PYTHON RETURNS THE VALUE g BECAUSE PYTHON ALSO COUNTS IN NEGATIVE DIRECTION FOR INDEXES, SO THE LAST LIST IS [-1] AND g ELEMENT IS [-2] COUNTING TO LEFT
print "g element counting to left =", q[-1][-2]