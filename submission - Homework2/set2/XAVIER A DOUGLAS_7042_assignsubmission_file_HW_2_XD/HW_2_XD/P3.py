
h = 0.010
i = 0.0

xivalue = []
for i in range(0,100,1):
	xi = 1.0 + i*h
	xivalue.append(("%.2f"%(xi)))
print("xivalue =",xivalue)
