v0= 1
g = 9.81 
n = 11
t = 0

tlist=[2*v0/g*x/n for x in range(n) ]
# print tlist

print "t     y(t)"
for t in tlist:
	y=v0*t-0.5*g*t**2
	print "%.4f\t%.4f"%(t,y)
