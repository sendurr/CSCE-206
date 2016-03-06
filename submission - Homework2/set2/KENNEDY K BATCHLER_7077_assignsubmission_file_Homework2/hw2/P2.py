v0=1
g=9.81
n=11
t=0

end=2.0*(v0/g)
i=0
step=end/11

print "t\t\ty(t)"
while t < end:
	y = (v0*t)-(0.5*g*t**2)
	print"%f/t%f"%(t,y)
	t+=step