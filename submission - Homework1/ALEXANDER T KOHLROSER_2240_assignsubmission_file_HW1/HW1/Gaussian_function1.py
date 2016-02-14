import math
#Builds environment

m = 0
s = 2
x = 1
#sets variables

if s in range(0, 100000):
	fx = (1/(math.sqrt(2 *math.pi) * s))*math.exp((-1/2)*((x-m)/s)**2)
	print(fx)
	#calculates if s is greater than or equal to 0

else:
	print("s must be greater than 0")
	#otherwise informs the user that s must be greater than 0