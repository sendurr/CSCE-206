#Rachel Smoak
#Homework 2
#14 February 2016

#Problem 5
#Polynomials and loops
from sympy import * #need this to do symbolic math and treat variables as variables
r = [-1, 1, 2] #list of roots
x = symbols('x') #define x as a symbol
p = 1 #beginning product number
for i in r: #start a for loop
	p *= (x-i) #multiply (x-r) for all roots
print p, '=', expand(p) #print the factored and expanded versions