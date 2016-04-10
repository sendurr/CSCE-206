'''################################################################################
    CSCE 206 Lab9  , Exercise Q1
    using classes - function overloading
    
    Author:   Sendurr Selvaraj
    Email:    sendurr@hotmail.com
################################################################################'''

from math import * 

class Sum:
	def __init__(self, function , M , N):
		self.function=function
		self.N=N
		self.M=M


	def __call__(self, x):
		f , N , M = self.function , self.N , self.M
		print ("The ouput of ") + str(f) + (" when x = ") + str(x) + (" M = ") + str(M) + (" N = ") + str(N) + (" is ") + str(f(N , M , x))
		print ("The first neglect term of ") + str(f) + (" when x = ") + str(x) + (" M = ") + str(M) + (" N = ") + str(N) + (" is ") + str(f(M+1 , M+1 , x))

def term(N, M , x):
	result =0
	for i in range(N,M+1):
		result = result + (-x)**i
		#print ("The value of x = %d and i = %d and result = %d" %(x,i, result))
	return result

def sinx(M, N , x):
	result =0
	for i in range(M,N+1):
		result = result + exp(-x)
		#print ("The value of x = %d and i = %d and result = %d" %(x,i, result))
	return result

def exp_x(M, N , x):
	result =0
	for i in range(M,N+1):
		result = result + sin(x)
		#print ("The value of x = %d and i = %d and result = %d" %(x,i, result))
	return result



#	def print_content(self):
#		print ("The value of a = " + str(self.a))
#		print ("The value of w = " + str(self.w))

f1 = Sum(term, 0 , 1)
f1(6)
f2 = Sum(sinx, 0 , 5)
f2(pi)
f2(30*pi)
f2.N=10
f2(pi)
f2(30*pi)
f2.N=20
f2(pi)
f2(30*pi)
f3 = Sum(exp_x, 0 , 5)
f3(1)
f3(3)
f3(5)
f3.N=10
f3(1)
f3(3)
f3(5)
f3.N=20
f3(1)
f3(3)
f3(5)



'''################################################################################
    End of Program
################################################################################'''
