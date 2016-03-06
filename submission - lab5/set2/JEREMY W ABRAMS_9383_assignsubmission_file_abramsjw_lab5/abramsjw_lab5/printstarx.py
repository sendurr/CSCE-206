# Jeremy Abrams
# CSCE 206
# Lab 5 - printstarx.py
# February 9, 2016

# Define printstarx function, which will take in the number of stars to print
# and the number of rows to print. The default row value is set to 1.
def printstarx(n, row=1):
	for i in range (0, row):
		print "*"*n

# Print output to test functionality
print "Test 1: "
printstarx(10)
print "\nTest 2: "
printstarx(10, 5)