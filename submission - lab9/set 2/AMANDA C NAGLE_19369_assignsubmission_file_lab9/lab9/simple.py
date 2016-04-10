class simple:
	def __init__ (self, i):
		self.i=i
	def double(self):
		return self.i+self.i
s1=simple(4)
print s1.double()

s2= simple('Hello')
print s2.i
s2.i= 100