# Jeremy Abrams
# CSCE 206
# Homework 2 - P2.py
# February 9, 2016

# Initialize the given values for the formula
v0 = 1
g = 9.81
n = 11
tolerance = 1E-14

# Create empty t and y lists
t_values = []
y_values = []

# Solve for t
dt = (2*v0/g-0)/(n-1)
t = 0

# Add t values to t_values list
while t <= 2 * v0/g+tolerance:
	t_values.append(t)
	t = t + dt

# Add y values to y_values list by using the provided formula
y_values = [v0 * t - 0.5 * g * t ** 2 for t in t_values]


# Print out the t values and y values
for counter in range(0, n):
	print '%8.3f %8.3f' % (t_values[counter], y_values[counter])