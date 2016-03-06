# Jeremy Abrams
# CSCE 206
# Lab 4 - Sum For Loop
# February 4, 2016

# Initialize variables to use for the for loop calculation
s = 0
M = 101

# For loop to sum up all of the fractions 
for k in range(1, M):
	s = s + (1.0/k)

print s