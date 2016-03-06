v0 = 1
g = 9.81
n = 11
t_end = 2*v0/g
t_step = t_end/n

for i in range(n):
	t = t_step * i
	y = v0*t - 0.5*g*t**2
	print "%2.2f %2.2f"%(t,y)