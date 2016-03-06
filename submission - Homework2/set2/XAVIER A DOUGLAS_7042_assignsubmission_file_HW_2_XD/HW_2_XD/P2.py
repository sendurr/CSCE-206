
v0 = 1
g = 9.81
n = 11
r = ((2.0*v0)/g)

tvalue = []
x = 0
for x in range(1,11):
	p = r/x
	tvalue.append(p)
#print(sorted(tvalue))

for t in sorted(tvalue):
	y = v0*t - 0.5*g*t**2
	print ("%.10f"%(t),"%.10f"%(y))

