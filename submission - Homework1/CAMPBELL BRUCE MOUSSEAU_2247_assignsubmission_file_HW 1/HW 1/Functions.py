x = set([1,3,8,10,14,10,20,25])
y = set([3,3,8,10,15,20,33,55,88])
a = x.intersection(y)
print (a)

b = x.union(y)
print (b)

z = x-y
t = y-x

print (z,t)