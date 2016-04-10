# Jeremy Abrams
# CSCE 206
# Lab 9 - F.py
# March 27, 2016

from math import * 

class F:
	total = 0.0
	def __init__(self, a, w):
		self.a = a
		self.w = w

	def value(self, x):
		self.x = x
		self.total = exp((0.-self.a)*self.x) * sin(self.w*self.x)
		return self.total

f = F(a=1.0, w=0.1)
print f.value(x = pi)
f.a = 2.0
print f.value(pi)