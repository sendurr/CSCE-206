#Question 5

X = {1, 3, 8, 10, 14, 20, 25}
Y = {3, 3, 8, 10, 15, 20, 33, 55, 88}

intersection = X & Y
print ("intersection: ", intersection)

union = X | Y
print ("union: ", union)

noty = X - Y
print ("In X but not in Y (X-Y): ", noty)

notx = Y - X
print ("In Y but not in X (Y-X): ", notx)