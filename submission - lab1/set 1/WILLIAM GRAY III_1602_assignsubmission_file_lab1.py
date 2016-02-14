i1= 2.33
i2= -2
i3="32233"
i4='I am a boy'
print(i1)
print(i2)
print(i3)
print(i4)
print(i1,i2,i3,i4)


array1= [3,4.0,34,-5,23]
print(array1[1:][::2])				# [1:] signifies that the print wll start on the 1th value, with the first value being the 0th
									# [::2] means every 2nd value after the start point will be a part of the list

list1= ["good", "very good", "excellent"]
print([list1[0], list1[-1]])	


import numpy
matrix1=numpy.zeros((3,3))				# numpy is an app for creating matricies
matrix1[0]=[1,2,3]						# the command [numpy.zeros] creates an empty array of the specified 
matrix1[1]=[4,5,6]
matrix1[2]=[7,8,9]
print(matrix1)