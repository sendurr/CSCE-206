def fib(n):
	cur = 1
	old = 1
	i = 1
	while (i<n):
		cur, old, i=cur+old, cur, i+1
	return cur
for i in range(1000):
	print (fib(i))