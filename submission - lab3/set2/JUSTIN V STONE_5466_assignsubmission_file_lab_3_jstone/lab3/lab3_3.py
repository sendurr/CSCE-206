import random
x=[int(300*random.random()) for i in xrange(300)]

i=0
while i in range(0, len(x)):
	if x[i]%3==0 and x[i]%7==0:
		print x[i]
	i+=1
