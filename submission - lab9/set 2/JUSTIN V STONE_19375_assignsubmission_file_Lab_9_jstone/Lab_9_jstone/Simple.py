#Exercise 7.2

class Simple:
	def __init__(self, n):
		self.n = n

	def double(self):
		self.n= self.n+self.n
		return self.n

s1 = Simple(4)
for n in range(4):
	s1.double()
print s1.n

s2 = Simple('Hello')
s2.double()
print s2.n
s2.n = 100
print s2.n