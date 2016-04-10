class Sum(object):

	def __init__(self,f,M,N):
		self.f = f
		self.M = M
		self.N = N


	def __call__(self,x):
		S = 0
		for k in range(self.M,self.N+1):
			S += (self.f)(k,x)
		first_neglected_term = (self.f)(self.N+1,x)
		print first_neglected_term
		return S


def term(k,x):
	return (-x)**k

S = Sum(term,M=0,N=100)
x = 0.5
print S(x)

