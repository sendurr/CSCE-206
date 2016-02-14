#Rachel Smoak
#HW1 Exercise 1.10

#import math
from math import *
#define a function; used x, m, and s as parameters instead of seperately defining m and s
def f(x,m,s):
	answer = exp(-0.5*((x-m)/s)**2)/(sqrt(2.*pi)*s)
	return answer
	pass
#make sure not to trigger integer math
print f(1.,0.,2.)
