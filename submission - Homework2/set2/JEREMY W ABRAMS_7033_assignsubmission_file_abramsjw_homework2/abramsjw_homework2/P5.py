# Jeremy Abrams
# CSCE 206
# Homework 2 - P5.py
# February 9, 2016

# Initialize roots list
roots = [-1, 1, 2]

# Initialize p_x and x variables for polynomial product
p_x = 1
x = 10

# Loop through roots list and multiply the product by (x-every root value)
for r in roots:
	p_x = (x-r)*p_x
	print p_x

# Print out the final product
print "\nFinal product: ", p_x