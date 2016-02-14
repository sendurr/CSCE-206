# Jeremy Abrams
# CSCE 206
# Set Operations - Homework 1
# January 22, 2016

# Create sets in X and Y
X=set([1,3,8,10,14,10,20,25])
Y=set([3,3,8,10,15,20,33,55,88])

# Store set operations in separate variables for printing
union = X | Y
intersect = X & Y
x_diff = X-Y
y_diff = Y-X

# Print the set operation results
print union, '\n', intersect, '\n', x_diff, '\n', y_diff