g=9.81
n=11.0
v_0=1.0

t=0
dt=(2*v_0/g)/n
while t <= 2*v_0/g:
	print(t, v_0*t + 0.5*g*t**2)
	t += dt