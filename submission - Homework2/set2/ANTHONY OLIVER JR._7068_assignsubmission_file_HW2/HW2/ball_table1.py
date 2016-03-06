t=0
v0=1
g=9.81
n=11
while t <= 2*v0/g:  
	y=v0*t-0.5*g*t**2
	print (t , y)
	t = t + n

