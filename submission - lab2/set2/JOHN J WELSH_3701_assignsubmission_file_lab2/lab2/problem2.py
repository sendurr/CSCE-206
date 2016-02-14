#Lab 2, Problem 2 by John Welsh

# 2. create a 3 dimension matrix of  3X3X3 and store it into M3 variable
# the values are
# 1	1	1
# 1	1	1
# 1	1	9

# 2	2	2
# 2	8	2
# 2	2	2

# print the 8, 9 using the M3 variable with indexes

import numpy as np 											#Import numpy
M3_1 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 9]])			#Create First Array
M3_2 = np.array([[2, 2, 2], [2, 8, 2], [2, 2, 2]])			#Create Second Array
M3 = np.dstack((M3_1,M3_2))									#Stack Arrays into 3D
print M3[1,1,1], M3[2,2,0]