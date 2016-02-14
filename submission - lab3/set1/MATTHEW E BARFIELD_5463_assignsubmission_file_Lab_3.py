print "Question 1"
L1={2,3,4,10}
L2={5,3,4,9,10,15}

print "In Both L1 And L2: ", L1 & L2
print "In Either L1 or L2 But Not Both: ", L1 ^ L2
print "In L1 But Not In L2: ", L1-L2
L3 = L1 | L2
print "Merge of L1 and L2: L3 = ", L3

L1 = list(L1)
L2 = list(L2)

L2.append(103)
L2.append(20)
L2.append(34)

print L2
print ("")

print "Question 2"
Var = 13
Step = 2
Sum = 0
while Var<1000:
	Sum += Var
	Var += Step
print Sum
print ("")

print "Question 3"
import random
x = [int(300*random.random()) for i in xrange(300)]

i=0
while i in range(0,len(x)):
	if x[i]%3==0 and x[i]%7==0:
		print x[i]
	i+=1

