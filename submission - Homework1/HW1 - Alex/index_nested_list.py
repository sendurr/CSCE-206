# Alexis Thompson-Klemish
#

q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]

# print the letter a
print q[0][0]

# print the list ['d', 'e', 'f']
print q[1]

# print the last element h
print q[-1][-1]

#print the d element
print q[1][0]

#explain why q[-1][-2] has the value g
print "negative indexes count from the right, not the left so q[-1] produces the rightmost list and q[-1][-2] produces the second to last element in the last list"
