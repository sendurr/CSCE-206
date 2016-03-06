# Jeremy Abrams
# CSCE 206
# Homework 2 - P4.py
# February 9, 2016

# Initialize a and b
a = [1, 3, 5, 7, 11]
b = [13, 17]

# Concatenate a and b and store it into c
c = a + b

print "The concatenation of a and b is: ", c

# Set the first index value of B to -1
b[0] = -1

# Store a+1 values into d
d = [e+1 for e in a]
print "The values of a+1 are: ", d 

# Add the value of b[0] + 1 to the end of d
d.append(b[0] + 1)

# Add the value of b[-1]+1 (or the last item in b) into d
d.append(b[-1] + 1)

# Print out the last two items that were added
print "The appended values in d are: ", d[-2:]