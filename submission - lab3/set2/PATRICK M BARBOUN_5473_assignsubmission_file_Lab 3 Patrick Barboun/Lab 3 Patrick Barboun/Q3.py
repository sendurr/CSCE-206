import random

x = [int(300*random.random()) for i in xrange(300)]

z=0

while z<len(x):
	if x[i]%3==0 and x[i]%7==0:
		print x[i]
	z+=1

