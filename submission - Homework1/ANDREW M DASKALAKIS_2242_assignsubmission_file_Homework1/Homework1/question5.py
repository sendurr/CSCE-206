from math import *
from sets import Set

#########################################
#		Sets the boring way
#########################################
print "boring sets"

q = Set([1,3,8,10,14,10,20,25])
w = Set([3,3,8,10,15,20,33,55,88])

a = q.intersection(w)
print "Intersection = " ,a

b = q.union(w)
print "union = " ,b

c = q.difference(w)
print "X-Y = " ,c

d = w.difference(q)
print "Y-X = " ,d


#########################################
#		Cool Sets
#########################################
print "cool sets"

#########################################
#		Intersection
#########################################

x = [1,3,8,10,14,10,20,25]
y = [3,3,8,10,15,20,33,55,88]
intersection = []

for i in range(0,len(x)):									#checks all elements in x
	for j in range(0,len(y)):								#checks all elements in y
		if x[i] == y[j] and x[i] not in intersection:		#checks if x at step i is equal two y at step j are equal and if x at step i is not already in the intersection array
			intersection.append(x[i])						#if these are both true this line adds the value at x at step i to the intersection array 

print "intersection = " ,sorted(intersection)

#########################################
#		Union
#########################################

union = []

#adds values from x and y if they are not already in the union array
for i in range(0,len(x)):									
	if x[i] not in union:
		union.append(x[i])

for j in range(0,len(y)):
	if y[j] not in union:
		union.append(y[j])

print "union = " ,sorted(union)

#########################################
#		X-Y
#########################################

f = []
for i in range(0,len(x)):
	if x[i] not in y:
		f.append(x[i])

print "X-Y = " , sorted(f)


g = []
for j in range(0,len(y)):
	if y[j] not in x:
		g.append(y[j])

print "Y-X = " , sorted(g)
