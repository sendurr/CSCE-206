'''################################################################################
    CSCE 206 Lab9  , Exercise Q2
    using classes - function overloading
    
    Author:   Sendurr Selvaraj
    Email:    sendurr@hotmail.com
################################################################################'''

from math import * 

class Simple:
	def __init__(self, i):
		self.i=i


	def double(self):
		self.i = self.i + self.i

#	def print_content(self):
#		print ("The value of a = " + str(self.a))
#		print ("The value of w = " + str(self.w))

s1 = Simple(4)

for i in range(4):
	s1.double()
	print ("The value of i in loop %d is %d: " %(i+1, (s1.i)))

s2 = Simple('Hello')
s2.double()
s2.double()
print ("The value of i is %s "%s2.i)
s2.i=100
print ("The value of i is %s "%s2.i)



'''################################################################################
    End of Program
################################################################################'''
