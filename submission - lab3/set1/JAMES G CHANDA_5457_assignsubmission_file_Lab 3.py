print "*****Question 1*****"
#1): play with list and set

L1= {2, 3, 4, 10}
L2= {5,3,4,9,10,15}

print "L1:", L1
print "L2:", L2
print "Intersection:" , L1 & L2
print "Exists in either:" , L1 ^ L2
print "L1 but not L2:", L1-L2
L3 = L1 | L2
print "L3:", L3
L2 = list(L2)
L2.append(103)
L2.append(20)
L2.append(34)
print "New L2:", L2



print ""
print "*****Question 2*****"
#2): while loop application, starting with 13, add all the odd numbers from 13 up
#to 999. save it to variable sum
var = 13
step = 2
var_sum = 0
while var <1000:
	var_sum += var
	var += step
print var_sum

	
print ""
print "*****Question 3*****"
import random
x=[int(300*random.random()) for i in xrange(300)]
#use while loop to print out all numbers that have factors of 3 and 7
#i = 0

i=0
while i in range(0,len(x)):
	if x[i]%3==0 and x[i]%7 == 0:
		print x[i]
	i+=1
	
