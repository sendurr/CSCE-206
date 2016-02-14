#index a nested list
""" q[-1][-2] has the value of g because the [-1] calls the last element of
the list q, and the [-2] calls the second to last element of the sublist
called by the [-1] """

q = [['a','b','c'],['d','e','f'],['g','h']]

print q[0][0]
print q[1]
print q[-1][-1]
print q[1][0]

