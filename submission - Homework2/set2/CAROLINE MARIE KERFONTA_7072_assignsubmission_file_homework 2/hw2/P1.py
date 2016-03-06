def fib(n):
 a,b = 1,1000
 for i in range(n-1):
  a,b = b,a+b
 return a
print (fib(1000))