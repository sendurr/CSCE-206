#P6
import sys
v0=sys.argv[1]
try:
	v0=float(v0)
except:
	print"enter a valid number"
	sys.exit(-1)
g=9.81
t=sys.argv[2]
try:
	t=float(t)
except:
	print"enter a valid number"
	sys.exit(-1)
y=v0*5-0.5*g*t**2
print y

