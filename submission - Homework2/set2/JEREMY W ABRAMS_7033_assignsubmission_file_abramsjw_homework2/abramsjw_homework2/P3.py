# Jeremy Abrams
# CSCE 206
# Homework 2 - P3.py
# February 9, 2016

# Initialize variables
h = 0.01
xi = []

# Run a loop from 0 to 100 to calculate the x values between 1 and 2.
for i in range (0, 100):
	xi.append(1 + i*h)

# Print list
print xi