from math import *
print "#######################"
print "Q1"
print "#######################"


def printstar(n):
	for x in range(0,n):
		print "*",
	print ""

printstar(1)
printstar(10)
printstar(100)

print "#######################"
print "Q2"
print "#######################"

def printstarx(n,row = 1):
	for x in range(0,row):
		printstar(n)

printstarx(10)
printstarx(10,5)

print "#######################"
print "Q3"
print "#######################"

def checkprime(n):
	for x in range(2,n):
		if n%x == 0:
			return False
	return True


print checkprime(3)
print checkprime(255)