# Jeremy Abrams
# CSCE 206
# Lab 4 - Sum While Loop
# February 4, 2016

# Initialize variables for the while loop
s = 0
M = 100
k = 1

# Iterate from values 1 to 100 and add all 1/k values. 
while k <= M:
	s = s + (1.0/k)
	k = k + 1

#Print total
print s