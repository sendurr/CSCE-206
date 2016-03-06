def fib():
	a, b = 0, 1
	while 1:
		yield a
		a, b = b, a + b
a = fib()
a.next()
for i in range(0,1000):
	print "#%0.0f %2.0f"%(i+1,a.next())