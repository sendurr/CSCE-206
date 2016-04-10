from math import *
class F:
	def __init__(self,a,w):
		self.a= a
		self.w= w
	def value(self,x):
		return exp(-self.a*x)*sin(self.w*x)	

f=F(a=1.0,w=0.1)
print (f.value(x=pi))
f.a=2	
print (f.value(pi))




class Simple:
	def __init__(self,i):
		self.i=i
	def double(self):
		self.i = self.i + self.i
		return self.i
s1 = Simple(4)
for i in range(4):
	s1.double()
print (s1.i) #this only prints the i that was input

s2= Simple('Hello')
s2.double(); s2.double()
print (s2.i) #this only prints the i that was input. It doesn't show the double method
s2.i=100
print (s2.i)


print (s1.double())
print (s2.double())
