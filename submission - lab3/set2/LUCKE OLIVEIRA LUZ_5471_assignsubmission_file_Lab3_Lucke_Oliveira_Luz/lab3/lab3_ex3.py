# Name: Lucke Oliveira Luz		Assignment: Lab 3      Exercise: 3

import random
x = [int(300*random.random()) for i in xrange(300)]
i = 0
FACTORS = []

while i < len(x):
	if x[i]%3 == 0:
		FACTORS.append(x[i])
		i+=1
	else:
		if x[i]%7 == 0:
			FACTORS.append(x[i])
			i+=1
		else:
			i+=1
print "FACTORS =", FACTORS