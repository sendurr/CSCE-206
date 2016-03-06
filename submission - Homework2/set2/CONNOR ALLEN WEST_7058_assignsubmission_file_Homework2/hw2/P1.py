x = [0,1]
for i in range(1000-len(x)):
	x.append(x[i]+x[i+1])
print(x)