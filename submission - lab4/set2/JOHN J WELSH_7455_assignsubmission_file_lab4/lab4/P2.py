M = 1000
_sum_for = 0
for k in range(1,M+1):
	_sum_for += 1/float(k)
print _sum_for

_sum_while = 0
k = 0
while k < M:
	k += 1
	_sum_while += 1/float(k)
print _sum_while
