# Jeremy Abrams
# CSCE 206
# Homework 2 - P1.py
# February 9, 2016

# Initialize numlist with 0 and 1
numlist = [0, 1]

print numlist, "\n"

# Loop from 2 to 1000 since the first index you are appending starts at index 2.
for i in range(2, 1001):
	numlist.append(numlist[i-1]+numlist[i-2])

# Print final numlist
print numlist