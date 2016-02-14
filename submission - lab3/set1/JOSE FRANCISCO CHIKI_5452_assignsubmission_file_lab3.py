print "1.play with list and set"
L1=[2,3,4,10]
L2=[5,3,4,9,10,15]
l1={2,3,4,10}
l2={5,3,4,9,10,15}
print "intersections:", l1&l2
# print "in either L1 or L2, but not both:" l2.symmetric_difference(l1)	#this set opperation won't work for some reason
print "in L1 but not in L2:", l1-l2
print "union of l1 and l2:", l1|l2
L2.append(103)
L2.append(20)
L2.append(34)
print "L2 post append:", L2
print "2.while loop application"
c=11
while c<=999:
	c+=1
	SUM=c
	SUM=SUM+c
print SUM
print "3. while loop"
import random
x=[int(300*random.random()) for i in xrange(300)]
z=0
while z<=298:
	z+=1
	if x[z]%21==0: #if the numbers have factors of 3 and 7, they must have a factor of 21
		print x[z]