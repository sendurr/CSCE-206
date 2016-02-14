# Jeremy Abrams
# CSCE 206
# Interest Rate - Homework 1
# January 22, 2016

# Define interest rate function
def interestRate(initial, percent, years):

	# Store interest rate total in separate variable and print 
	total = initial*(1+(percent/100))**years
	print "%0.2f" % total

# Call interest rate function
interestRate(1000, 0.05, 3)