#Q1

from math import *

class F:

    def __init__(self, a, w):
        self.a = a
        self.w = w

    def value(self, x):
        a = self.a
        w = self.w
        return exp(-a * w) * sin(w * x)

#Q2
class Simple:
	def __init__(self,i):
		self.i = i
	def double(self,i):
		i = self.i
		return (i+1)
