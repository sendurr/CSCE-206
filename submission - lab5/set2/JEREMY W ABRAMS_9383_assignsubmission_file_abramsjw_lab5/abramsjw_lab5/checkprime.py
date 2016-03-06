# Jeremy Abrams
# CSCE 206
# Lab 5 - checkprime.py
# February 9, 2016

# Define function to test if n is divisible by any numbers. If so, return false.
# If n is not divisible by any numbers, return true.
def checkprime(n):
	for x in range(2, n-1):
		if (n%x==0):
			return False
	return True

# Test funcionality of checkprime
print checkprime(3)
print checkprime(255)
