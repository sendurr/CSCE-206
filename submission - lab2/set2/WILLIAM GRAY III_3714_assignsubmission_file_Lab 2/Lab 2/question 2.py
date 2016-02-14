import numpy
M3=numpy.zeros((2,3,3))			#numpy.zeroes((x,y,z)) specifies x as layers, y as rows, z as columns

M3[0]=[[1,1,1],[1,1,1],[1,1,9]]
M3[1]=[[2,2,2],[2,8,2],[2,2,2]]

print(M3[0,2,2],"\t",M3[1,1,1])			#use "\t" to make results neater and more readable
