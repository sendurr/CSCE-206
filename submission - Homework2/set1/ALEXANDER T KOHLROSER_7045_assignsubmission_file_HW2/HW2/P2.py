v0 = 1
g = 9.81
n = 11
t = 0

print "t", "     ", "y(t)"

while t < n:
	y = v0*t - 0.5*g*t*t
	print t, "     " , y
	t = t + 1
