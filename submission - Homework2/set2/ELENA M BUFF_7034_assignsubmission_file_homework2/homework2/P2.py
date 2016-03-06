v0=1.0 #initial velocity
g=9.81 #acceleration of gravity
t=0.0
def dist (t):
	return v0*t-0.5*g*t**2

f=(2.0*v0)/g
k=f/11
i=0

while t<f:
	print t,"\t\t\t\t\t\t",dist(t)
	t+=k