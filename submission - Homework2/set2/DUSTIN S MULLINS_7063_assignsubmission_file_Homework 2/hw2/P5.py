x = 5
p = 1	#Start at 1
roots = [-1,1,2]
for n in roots:
	p=(x-n)*p     #Outputs (5-(-1))*(5-1)*(5-2) = 72
print p