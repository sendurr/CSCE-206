# Name: Lucke Oliveira Luz				Assignment: Lab 9           Exercise: 3

from math import *
from prettytable import PrettyTable

class Sum:
	def __init__(self,f,M,N):
		self.f = f
		self.M = int(M)
		self.N = int(N)

	def __call__(self,x):
		f = self.f
		self.first_neglected_term = f(self.N + 1,x)
		S = 0
		for i in range(self.M,self.N+1):
			S += f(i,x)
		return S

def term(k,x):
	return (-x)**k

S = Sum(term,0,100)
x = 0.5
print S(x)
print S.first_neglected_term

def sin_taylor(k,x):
	return (-1)**k*x**(2*k+1)/factorial(2*k+1)

def exp_taylor(k,x):
	return (-x)**k/factorial(k)

def sum_page98(k,x):
	k = float(k)
	return (1/k)*(x/(1+x))**k

N = [5,10,20]
x_sin = [pi,30*pi]
Sum_sin = []
FNT_sin = []

for i in N:
	S_sin = Sum(sin_taylor,0,i)
	for j in x_sin:
		Sum_sin.append(S_sin(j))
		FNT_sin.append(S_sin.first_neglected_term)

x_exp = [1.0,3.0,5.0]
Sum_exp = []
FNT_exp = []

for i in N:
	S_exp = Sum(exp_taylor,0,i)
	for j in x_exp:
		Sum_exp.append(S_exp(j))
		FNT_exp.append(S_exp.first_neglected_term)

x_sum98 = [2.0,5.0,10.0]
Sum_98 = []
FNT_98 = []

for i in N:
	S_98 = Sum(sum_page98,1,i)
	for j in x_sum98:
		Sum_98.append(S_98(j))
		FNT_98.append(S_98.first_neglected_term)

table1 = PrettyTable(['Function','x','M','N','Sum','First Neg. Term'])
table1.add_row(['sin(x)',x_sin[0],0,N[0],Sum_sin[0],FNT_sin[0]])
table1.add_row(['sin(x)',x_sin[0],0,N[1],Sum_sin[2],FNT_sin[2]])
table1.add_row(['sin(x)',x_sin[0],0,N[2],Sum_sin[4],FNT_sin[4]])
table1.add_row(['sin(x)',x_sin[1],0,N[0],Sum_sin[1],FNT_sin[1]])
table1.add_row(['sin(x)',x_sin[1],0,N[1],Sum_sin[3],FNT_sin[3]])
table1.add_row(['sin(x)',x_sin[1],0,N[2],Sum_sin[5],FNT_sin[5]])

table2 = PrettyTable(['Function','x','M','N','Sum','First Neg. Term'])
table2.add_row(['exp(-x)',x_exp[0],0,N[0],Sum_exp[0],FNT_exp[0]])
table2.add_row(['exp(-x)',x_exp[0],0,N[1],Sum_exp[3],FNT_exp[3]])
table2.add_row(['exp(-x)',x_exp[0],0,N[2],Sum_exp[6],FNT_exp[6]])
table2.add_row(['exp(-x)',x_exp[1],0,N[0],Sum_exp[1],FNT_exp[1]])
table2.add_row(['exp(-x)',x_exp[1],0,N[1],Sum_exp[4],FNT_exp[4]])
table2.add_row(['exp(-x)',x_exp[1],0,N[2],Sum_exp[7],FNT_exp[7]])
table2.add_row(['exp(-x)',x_exp[2],0,N[0],Sum_exp[2],FNT_exp[2]])
table2.add_row(['exp(-x)',x_exp[2],0,N[1],Sum_exp[5],FNT_exp[5]])
table2.add_row(['exp(-x)',x_exp[2],0,N[2],Sum_exp[8],FNT_exp[8]])

table3 = PrettyTable(['Function','x','M','N','Sum','First Neg. Term'])
table3.add_row(['Sum of page 98',x_sum98[0],1,N[0],Sum_98[0],FNT_98[0]])
table3.add_row(['Sum of page 98',x_sum98[0],1,N[1],Sum_98[3],FNT_98[3]])
table3.add_row(['Sum of page 98',x_sum98[0],1,N[2],Sum_98[6],FNT_98[6]])
table3.add_row(['Sum of page 98',x_sum98[1],1,N[0],Sum_98[1],FNT_98[1]])
table3.add_row(['Sum of page 98',x_sum98[1],1,N[1],Sum_98[4],FNT_98[4]])
table3.add_row(['Sum of page 98',x_sum98[1],1,N[2],Sum_98[7],FNT_98[7]])
table3.add_row(['Sum of page 98',x_sum98[2],1,N[0],Sum_98[2],FNT_98[2]])
table3.add_row(['Sum of page 98',x_sum98[2],1,N[1],Sum_98[5],FNT_98[5]])
table3.add_row(['Sum of page 98',x_sum98[2],1,N[2],Sum_98[8],FNT_98[8]])

print table1
print table2
print table3