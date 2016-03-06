# Jeremy Abrams
# CSCE 206
# Lab 4 - Boundary Sum
# February 4, 2016

# Define matrix M and initialize total to 0.
M = [[1,2,3],[4,5,6],[7,8,9]]
total = 0

# Loop through every row and column of M and total the numbers up.
for i in range(0,3):
	for j in range(0,3):

		# Condition for not adding the middle number since it is not on the boundary
		if i==1 and j==1:
			total = total
		else:
			total = total + M[i][j]

# Print total
print "Boundary Sum: ", total