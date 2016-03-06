fib=[0,1]

for i in range(1,999):
	fib.append(fib[i]+fib[i-1])
print fib
#print len(fib)