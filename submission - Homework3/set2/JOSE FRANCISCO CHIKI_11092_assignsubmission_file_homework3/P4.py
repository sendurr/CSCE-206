t=raw_input("t=")
v0=raw_input("v0=")
try:
	t=float(t)
	v0=float(v0)
	y=v0*t-.5*9.81*t**2
	print "y(t)=",y
except:
	print "please input t and v0 values as numbers only"
	