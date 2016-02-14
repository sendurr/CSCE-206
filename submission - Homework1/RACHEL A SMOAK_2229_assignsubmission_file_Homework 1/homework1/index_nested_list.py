#Rachel Smoak
#HW1 Exercise 2.19

q = [['a','b','c'],['d','e','f'],['g','h']]
print 'Extract a'
# a is in the first position, row 0, column 0
print q[0][0]

#d, e, f is in row 1, all columns (so column can have : or be left out)
print 'Extract list'
print q[1][:]

#last element, row end -1, column end -1
print 'Extract h'
print q[-1][-1]

#d is in row 1, column 0
print 'Extract d'
print q[1][0]

print
print 'q[-1][-2] has the value g because it is indexing the element in the last row, second to last column, and g is in that position'