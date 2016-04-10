# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 21:50:13 2016

@author: Tret Burdette
"""

from math import *

class F:
	def __init__(self,a,w):
		self.a=a
		self.w=w
	def value(self,x):
		return exp(-self.a*x)*sin(self.w*x)


f=F(a=1.0,w=0.1)
print f.value(x=pi)
f.a=2
print f.value(pi)
