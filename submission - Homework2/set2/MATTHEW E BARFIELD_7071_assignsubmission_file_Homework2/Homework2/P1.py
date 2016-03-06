
def Fibo(n):
	if n == 1:
		return 1
	elif n == 0:
		return 0
	else:
		return fib(n-1) + fib(n-2)

def Fiboo():
	a,b = 0,1
	yield a
	yield b
	while True:
		a,b = b, a+b
		yield b

def Fibooo(Start, End):
	for value in Fiboo():
		if value > End: return
		if value >= Start:
			yield value

for i in Fibooo(0,1000):
	print i