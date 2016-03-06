v0 = 1.0
g = 9.81
n = 11

tend = 2*v0/g
tvar = tend/n

for i in range(n):
	t = tvar*i
	y = v0*t -0.5*g*t**2
	print "%3.4f %3.4f" %(t,y)