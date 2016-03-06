
def f(n):
 x,y = 0,1
 for i in range(n-1):
  x,y = y,x+y
 return x

for z in range(1,1001):
	if z >= 0:
		print (z,f(z))