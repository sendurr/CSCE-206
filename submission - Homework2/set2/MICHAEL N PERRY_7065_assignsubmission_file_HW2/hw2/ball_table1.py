v0=1
g=9.81
n=11

def y(t):
	answer = v0*t-0.5*g*t**2.0
	return answer

def frange(start,stop,step):
	i=start
	while i<stop:
		yield i 
		i +=step
print "%4s"%("t"),"%8s"%("y(t)")
for i in frange(0,2.0*v0/g,(2.0*v0/g)/n):
	y(i)
	print "%.4f"%(i),"%.4f"%(y(i))



