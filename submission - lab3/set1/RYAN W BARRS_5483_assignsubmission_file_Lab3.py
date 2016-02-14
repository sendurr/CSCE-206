#=====1=====#
L1 = {2,3,4,10}
L2 = {5,3,4,9,10,15}

print "numbers in both:", L1 & L2
print "numbers in either L1 or L2, not both:", L1 ^ L2
print "numbers in L1 but not in L2:", L1 - L2

L3 = L1 | L2
print "L3:", L3

L2 = [5,3,4,9,10,15]
L2.append(103)
L2.append(20)
L2.append(34)
print "Appended list:",L2

#=====2=====#
Sum = 0
num = 13
while num <=999:
	Sum += num
	num += 2
print "Sum =",Sum

#=====3=====#
import random
random=[int(300*random.random()) for i in xrange(300)]
for x in random:
	if x%3==0 and x%7==0:
		print x