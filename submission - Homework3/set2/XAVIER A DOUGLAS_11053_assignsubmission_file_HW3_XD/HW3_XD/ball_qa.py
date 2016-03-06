
t=input("t =")
v0=input("v0 =")
g=9.81
try:
	t=float(t)
	v0=float(v0)
	y = v0*t - 0.5*g*t**2
	print("y =",y)
except:
	print("input t & v0 must be numbers")