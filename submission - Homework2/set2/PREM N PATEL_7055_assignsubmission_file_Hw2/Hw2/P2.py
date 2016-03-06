t=0; v0 = 1.0; g = 9.81; n = 11
t_stop = 2*v0/g
dt = t_stop/float(n)

def y(t):
	y = v0*t-0.5*g*t**2
	return float(y)

print "%2s %7s"%("t", "y(t)")
while t <= t_stop:
	print "%5.4f %5.4f"%(t, y(t))
	t += dt