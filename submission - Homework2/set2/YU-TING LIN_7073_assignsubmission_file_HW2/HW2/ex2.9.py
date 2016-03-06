a=[1,3,5,7,11]
b=[13,17]
c=a+b
print c
print "This print combines list a and list b to a new list c"

b[0]=-1
d=[e+1 for e in a]
print d
print " This print gives a new list a where all the numbers in list a are added by 1"

d.append(b[0]+1)
d.append(b[-1]+1)
print d[-2:]
print "the first append(b[0]+1) gives a number of 0 because a new b[0] is assgined to be -1. So, -1+1=0"
print "the second append(b[-1]+1) gives a number of 18 because b[-1] counting backward is numer 17 and 17+1=18"