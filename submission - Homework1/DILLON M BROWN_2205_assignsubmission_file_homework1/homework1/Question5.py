#Takes the intersection of 2 sets and outputs common elements
#Dillon Brown

X = set([1,3,8,10,14,10,20,25])
Y = set([3,3,8,10,15,20,33,55,88])

intersection = X.intersection(Y)
print list(intersection)