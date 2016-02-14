
print "1"
L1=[2, 3, 4,10]
L2=[5,3,4,9,10,15]
L1set=set(L1)
L2set=set(L2)
print "Print out the numbers that exist in both variables L1 and L2 using set operations"
print L1set&L2set

print "Print out numbers that exist in L1 but not in L2."
print L1set-L2set

print "Print out numbers that exists in either L1 or L2, but not both using set operation"
i=0
j=0
for i in range(0, i<len(L1)-1):
    for j in range(0, j<len(L2)-1):
        if L1[i]!=L2[j]:
            print L1[i]
            j+=1
        i+=1
i=0
j=0
for i in range(0, i<len(L2)-1):
    for j in range(0, j<len(L1)-1):
        if L2[i]!=L1[j]:
            print L2[i]
            j+=1
        i+=1
print 'Print out numbers that exists in either L1 or L2, but not both using set operation'
L3=L1+L2

print "merge L1 and L2 and save it into variable L3"
print L3

L2.append(103)
L2.append(20)
L2.append(34)
print"Add the following numbers to L2,   103, 20, 34 using  append() function of list."
print L2

print '*'*15
print "2"
i=0
sum=0
for i in range(13,999,2):
    sum = sum + i
print sum

print '*'*15
print "3"
import random
x=[int(300*random.random()) for i in xrange(300)]
for j in range(0,300):
    if x[j]%4==0:
        print x[j],
    if x[j]%7==0:
        print x[j],