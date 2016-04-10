from math import exp, sin, pi

class F(object):

	def __init__(self, a, w):
		self.a = a
		self.w = w

	def value(self, x):
		return exp(-self.a*x)*sin(self.w*x)

f = F(1.0, 0.1)
print f.value(pi)
f.a = 2
print f.value(pi)