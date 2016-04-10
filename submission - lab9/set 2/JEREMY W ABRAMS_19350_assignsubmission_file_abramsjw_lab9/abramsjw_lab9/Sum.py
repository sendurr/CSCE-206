# Jeremy Abrams
# CSCE 206
# Lab 9 - Sum.py
# March 27, 2016

import sys
from math import * 

class Sum:
	total = 0.0
	first_neglected_term = 0.0

	def __init__(self, term, M, N):
		self.term = term
		self.M = M
		self.N = N

	def __call__(self, x):
		while self.M < self.N:
			self.total = self.total + self.term(self.M, x)
			self.first_neglected_term = self.total
			self.M = self.M + 1

		self.first_neglected_term = self.first_neglected_term + self.term((self.M+1), x)
		return self.total




def term1(k, x):
	return (-x)**k

S1 = Sum(term1, M=0.0, N=100.0)
x = 0.5
print ("When X = 0.5")
print S1(x)
print S1.first_neglected_term

