#X'Avier Douglas - Lab 5

#Q1
def printstar(n):
	print("*"*n),
	pass

printstar(1)
printstar(10)
printstar(100)


#Q2 
def printstarx(n,r):
	r = 1
	#couldnt figure out the row thing
	print(printstar(n),r)



#Q3
import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        print ('False')
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print('False')
        if n % i != 0:
        	print('True')
check_prime(3)
