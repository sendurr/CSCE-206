class Sum:
	def __init__(self, M, N):
		self.M = M
		self.N = N

	def f(self, x):
		for i in range(self.M, self.N):
			F = (-x)**i
			return F

	# def first_neglected_term(self):
		
	# def __call__(self):

S = Sum(M=0, N=100)
x = 0.5
print S.f(x)