'''Question 4: define an array based vectorization function sincos(x)
so that you can compute. this function will calculate the sin(cos(x)) for each value of the input vector/array x.'''

from numpy import *
def sincos(x):
	#result=...to be finished by you
	result = []
	for i in x:
		result.append(sin(cos(i)))
	return result

x= array([1,3,5,7,10.5])
y= sincos(x)

print y