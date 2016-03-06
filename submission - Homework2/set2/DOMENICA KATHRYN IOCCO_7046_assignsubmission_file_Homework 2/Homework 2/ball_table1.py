#Question 2--------------------
v0=1
g=9.81
t=0.0
stop= (2.0*(v0/g))
i=0
step=stop/11.0
print("t\t\ty(t)")
while t < stop:
	y=(v0*t)-(0.5*g*(t**2))
	t += step
	print("%f\t%f"%(t,y))