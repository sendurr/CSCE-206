import random
x=[int(300*random.random()) for i in range(300)]
i=0
#print x
#print i
while i < len(x):
	if x[i]%3==0 and x[i]%7==0:
		print (x[i])
	i += 1



