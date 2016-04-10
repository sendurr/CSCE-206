from math import * 
from math import sin
from math import exp

class F(object):

	def __init__(self, a, w):
		self.a = a
		self.w = w
	def value(self,x):
		a = self.a
		w = self.w
		return exp(-a*w)*sin(w*x)


f=F(a=1,w=0.1)
print (f.value(x=pi))
f.a=2
print (f.value(pi))

