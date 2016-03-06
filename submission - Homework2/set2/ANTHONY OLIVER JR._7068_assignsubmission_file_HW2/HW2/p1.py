def f():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b
for index, x in enumerate (f()):
	print ('{i:3}: {f:3}'.format(i=index, f=x))
	if index == 1000  :
		break