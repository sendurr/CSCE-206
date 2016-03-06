v_0 = 1.
g = 9.81
n = 11
h = 2*v_0/g/n
t = 0

for i in range(n+1):
	print "%10.3f %10.3f" % (t, v_0*t-0.5*g*t**2)
	t += h
