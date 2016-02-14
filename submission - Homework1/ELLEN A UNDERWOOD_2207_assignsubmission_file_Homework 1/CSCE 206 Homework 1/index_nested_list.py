q=[['a','b','c'],
['d','e','f'],
['g','h']]
print q[0][0]
print q[1]
print q[2][1]
print q[1][0]

print q[-1][-2]

#q[-1][-2] is g because q[1][2] is out of range therefore 
#it needs to move back one space each. 
#It starts from the end of the list and moves backward.