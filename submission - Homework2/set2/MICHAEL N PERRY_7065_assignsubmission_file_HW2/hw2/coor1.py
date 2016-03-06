h=0.01

def x(i):
	answer=1+i*h
	return answer
print "x(i)"
for t in range(0,101,1):
	x(t)
	print "%.2f"%(x(t))
