#Rachel Smoak
#3 April 2016
#Lab 9

#Question 2

class Simple:
	"""Implements the function Simple"""
	def __init__(self, i):
		self.i = i
	def double(self):
		global i 		
		self.i = self.i + self.i

s1 = Simple(4)
for i in range(4):
	s1.double()
print s1.i

s2 = Simple('Hello')
s2.double(); s2.double()
print s2.i
s2.i = 100
print s2.i