import random

x=[int(300*random.random()) for i in xrange(300)]
print x
print len(x)

i=0
#while i < len(x):
#    if x[i]%7==0 and x[i]%3==0:
#	  i+=1
while i < len(x):
	i +=1
	print x[i]%7==0 and x[i]%3==0
	

