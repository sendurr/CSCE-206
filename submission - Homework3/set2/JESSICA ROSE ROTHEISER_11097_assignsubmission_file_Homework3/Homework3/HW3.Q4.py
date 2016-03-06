g=9.81
def y(v0,t,g):
	y=v0*t-0.5*g*t**2
	print (y)

v0=raw_input("v0=?")
v0=float(v0)

t=raw_input("t=?")
t=float(t)

print(y(v0,t,g))