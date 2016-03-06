
v0=1
g=9.81
t=0


intervalend = 2 * (v0/g)
intervalbegin = 0
n = intervalend/11

while t < intervalend:
	yt = (v0*t) - (.5 * g * t**2)
	print ("%f\t%f" % (t, yt))
	t+=n
