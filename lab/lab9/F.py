'''################################################################################
    CSCE 206 Lab9  , Exercise Q1
    using classes
    
    Author:   Sendurr Selvaraj
    Email:    sendurr@hotmail.com
################################################################################'''

from math import * 

class F:
	def __init__(self, a, w):
		self.a=a
		self.w=w

	def value(self,x):
		return (exp(-self.a * x) * sin(self.w * x))

#	def print_content(self):
#		print ("The value of a = " + str(self.a))
#		print ("The value of w = " + str(self.w))

f = F(a = 1.0, w = 0.1)
print ("printing value of f.value(x=pi) : " + str((f.value(x = pi))))
f.a=2
print ("printing value of f.value(pi) after a=2 : " + str((f.value(pi))))


'''################################################################################
    End of Program
################################################################################'''
