#Rachel Smoak
#3 April 2016
#Lab 9

#Question 1

class F:
	"""Implements the function f(x;a,w)"""
	def __init__(self, a, w): #define using class name and parameter list, see below
		self.a = a
		self.w = w
	def value(self,x):
		f = exp(-1*self.a*x)*sin(self.w*x)
		return f

from math import *
f = F(a=1.0, w = 0.1) #initialize the values in F so I can use the values later
print f.value(x=pi)
f.a = 2 #redefine a in F
print f.value(pi)