#lab5_2
def printstar(n):
	i=1
	for i in range(1,n+1):
         print '*',
def printstarx(n,row=1):
	i=0
	for i in range(0,row):
		printstar(n)
		print ""

print''
print "First test"
printstarx(10)
print''
print "Second test"
printstarx(10,row=5)