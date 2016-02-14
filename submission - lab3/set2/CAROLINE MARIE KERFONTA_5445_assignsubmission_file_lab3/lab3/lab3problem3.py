import random
x=[int(300*random.random()) for i in xrange(300)]
if x%3 == 0 and x%7==0:
	print (x)