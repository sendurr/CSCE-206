z = [0,1]
f = 2
while f < 1000:
	z.append(z[f-2]+z[f-1])
	f+=1
print z



