from math import factorial, pi
from math import sin as sn
from math import exp as xp
class Sum:
	def __init__(self,f,M,N):
		self.f = f
		self.M = int(M)
		self.N = int(N)
	def __call__(self,x):
		total = 0
		f = self.f
		M = self.M
		N = self.N
		for i in range(M,N+1):
			total += f(i,x)
		self.first_neglected_term = f(N+1,x)
		return total

def term(k,x):
	return (-x)**k
S = Sum(f=term, M=0, N=100)
x = 0.5
print S(x)
print S.first_neglected_term

def sin(k,x):
	return float(((-1)**(k-1))*(x**(2*k-1)))/float(factorial(2*k-1))
sin_approx = []; Number = []; Exponent = []
sin_error = []
sin_first_neglected_term = []
for x in [pi,30*pi]:
	for N in [5,10,20]:
		Tsin = Sum(f=sin, M = 1, N = N)
		Exponent.append(N)
		Number.append(x)
		sin_approx.append(Tsin(x))
		sin_error.append(sn(x)-Tsin(x))
		sin_first_neglected_term.append(Tsin.first_neglected_term)

print "Results for Taylor Expansion of sin(x):\n%10s %10s %40s %40s %40s"\
% ("x", "N", "Value", "Error", "First Neglected Term")
for i in range(len(Number)):
	print "%10.5f %10.0f %40.4f %40.5f %40.5f"\
	% (Number[i], Exponent[i], sin_approx[i], sin_error[i], sin_first_neglected_term[i])

def exponential(k,x):
	return float(((-1)**k)/float(factorial(k)))*(x**k)
exp_approx = []; Number = []; Exponent = []
exp_error = []
exp_first_neglected_term = []
for x in [1,3,5]:
	for N in [5,10,20]:
		Texp = Sum(f=exponential, M = 0, N = N)
		Exponent.append(N)
		Number.append(x)
		exp_approx.append(Texp(x))
		exp_error.append(xp(-x)-Texp(x))
		exp_first_neglected_term.append(Texp.first_neglected_term)

print "Results for Taylor Expansion of e**-x:\n%10s %10s %40s %40s %40s"\
% ("x", "N", "Value", "Error", "First Neglected Term")
for i in range(len(Number)):
	print "%10.5f %10.0f %40.4f %40.5f %40.5f"\
	% (Number[i], Exponent[i], exp_approx[i], exp_error[i], exp_first_neglected_term[i])



