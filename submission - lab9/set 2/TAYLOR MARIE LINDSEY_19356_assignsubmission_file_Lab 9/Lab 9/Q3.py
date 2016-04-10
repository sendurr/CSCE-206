
def term(k,x):
	return (-x)**k

S=Sum(term, M=0, N=100)
x=0.5
print S(x)

print S.first_neglected_term
