v0=1.0
g=9.81
n=11
step = ((2.0*v0)/g)/(n-1)
for i in range(0,11):
	t = step*i
	y=(v0*t) - (0.5*g*t**2)
	print("%f, %f"%(t,y))


