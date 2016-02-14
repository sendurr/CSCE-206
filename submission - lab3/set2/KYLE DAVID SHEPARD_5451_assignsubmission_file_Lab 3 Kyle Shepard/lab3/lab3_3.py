import random

x=[int(300*random.random()) for i in xrange(300)]

sortedx=sorted(x)

for y in sortedx:
	if(y%3==0):
		print y 
	if(y%7==0):
		print y
