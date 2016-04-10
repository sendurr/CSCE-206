'''################################################################################
    CSCE 206 Homework5  , Exercise Q3
    stack operations
    
    Author:   Sendurr Selvaraj
    Email:    sendurr@hotmail.com
################################################################################'''

from math import * 

class stack:
	def __init__(self):
		self.list=[]

	def push(self , x):
		list = self.list
		list.insert(0,x)
		#print list

	def pop(self):
		list = self.list
		if(len(list) > 0):
			print list[0]
			del list[0]
		else:
			print "The stack is empty!"

s1 = stack()
s1.push(5)
s1.push(6)
s1.pop()
s1.push(7)
s1.pop()
s1.pop()
s1.pop()


'''################################################################################
    End of Program
################################################################################'''
