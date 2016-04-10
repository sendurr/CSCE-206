'''################################################################################
    CSCE 206 Homework5  , Exercise Q2
    quadratic equation
    
    Author:   Sendurr Selvaraj
    Email:    sendurr@hotmail.com
################################################################################'''

from math import * 

class quadratic:
	def __init__(self, a, b , c):
		self.a=a
		self.b=b
		self.c=c

	def roots(self):
		a , b , c = self.a , self.b, self.c
		try:
			sub_result = sqrt((b**2) - (4 * a *c))
		except:
			print("Cannot perform sqrt of negative number, try with new coefficients")
			exit()
		root1 = ((-b) + sub_result) / (2 * a)
		root2 = ((-b) - sub_result) / (2 * a)
		print ("The roots of the quadratic equation %dx^2 + %dx + %d are %.2f & %.2f" %(a,b,c,root1,root2))

	def quad_result(self , x):
		a , b , c = self.a , self.b, self.c
		return (a*(x**2) + (b*x) + c)

	def quad_table(self, l , r):
		print ('-' * 25)
		print ('%-12s %-14s' % ('x', "f (x)"))
		print ('-' * 25)
		for i in range (l ,r+1):
			result = self.quad_result(i)
			print ("%-12d %-.2f"  %(i,result))
		print ('-' * 25)


q1 = quadratic (1 , 2, 3)
q1.quad_table(3 , 10)
q1.roots()





'''################################################################################
    End of Program
################################################################################'''
