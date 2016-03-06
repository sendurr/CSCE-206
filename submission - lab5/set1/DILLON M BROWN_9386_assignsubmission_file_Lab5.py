#Lab 5 Q1

def printstar(n):
    print '*'*n
    return
printstar(1)
printstar(10)
printstar(100)
print '--------------------------------'

#Q2

def printstarx(n,row=1):
    for i in range(row):
        printstar(n)
    return

printstarx(10)
printstarx(10,5)
print '--------------------------------'
#Q3
def checkprime(n):
    for i in xrange(2,n):
        if n%i == 0:
            return False
    return True

print 3, checkprime(3)
print 255, checkprime(255)
