a=[0,1]
i=2
while i<1000:
	a.append(a[i-2]+a[i-1])
	i+=1
print(a)