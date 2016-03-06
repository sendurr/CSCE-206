def f(n):
	x=0
	y=1
	for i in range(0,n):
		temp=x
		x=y
		y=temp+y
	return x
for z in range(0,1000):
	print(f(z))