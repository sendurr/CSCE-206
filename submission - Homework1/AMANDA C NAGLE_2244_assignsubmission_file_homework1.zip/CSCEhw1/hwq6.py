x= set([1,3,8,10,14,10,25])
y= set([3,3,8,10,15,20,33,55,88])
# calculate intersect, union, x-y, y-x
a= x & y
b= y | x
c= x-y
d= y-x
#print results
print 'intersect:', a
print 'union:', b
print 'in x but not y:', c
print 'in y but not x:', d



