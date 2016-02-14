# Alexis Thomson-Klemish
#

x = set([1, 3, 8, 10, 14, 10, 20, 25])
y = set([3, 3, 8, 10, 15, 20, 33, 55, 88])

union = x | y
print union

intersection = x & y
print intersection

print "in a and not in b", x-y
print "in a and not in b", y-x