#1
print ("1.")
L1=[2,3,4,10]
L2=[5,3,4,9,10,15]
print ('Numbers in both:', set(L1).intersection(set(L2)))
print ('Numbers in either, but not both:',set(L1).union(set(L2)) - set(L1).intersection(set(L2)))
print ('Numbers in L1 but not L2:',set(L1)-set(L2))
L3=L1+L2
print (L3)
new=L2.append([103,20,34])
print(L2)
print ()

#2
print ("2.")
#x=range(13,1000,2)
#i=0
#while i<len(x):
#	i+=1
#print (sum(x))
mySum=13
num=2
while num<1000:
	mySum+=num
	num+=2
print (mySum)
print ()

#3
print ("3.")
import random
x=[int(300*random.random()) for i in xrange(300)]
#print(x)
i=0
while i<300:
	if i%3==0 and i%7==0:
		print (i)
	i+=1
