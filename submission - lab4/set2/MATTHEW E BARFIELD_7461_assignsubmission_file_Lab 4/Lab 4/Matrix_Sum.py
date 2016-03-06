print 'Computing a Matrix Sum'
print ('')

m=[[1,2,3],
[4,5,6],
[7,8,9]]
for row in m:
	print row
print ('')

#print m[0][0], m[1][0], m[2][0], m[0][2], m[1][2], m[2][2]

def sumColumn(m, column):
    total = 0
    for row in range(len(m)):
        total += m[1][0]
    return total

column = 0
print 'Sum of Elements in Column: ', column
print(sumColumn(m, column))
print ('')

import numpy as numpy

print ('Sum of Elements in Columns: ')
def sumColumn(m):
    return numpy.sum(m, axis=0)
print (sumColumn(m))
print ('')

print ('Sum of Elements in Rows: ')
def sumRow(m):
    return numpy.sum(m, axis=1)
print (sumRow(m))


