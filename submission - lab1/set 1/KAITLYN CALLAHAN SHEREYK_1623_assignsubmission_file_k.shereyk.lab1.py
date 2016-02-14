x=2.33
y=-2
z="32233"
k='I am a boy'
print (x,y,z,k)

array1=(3,4,0,34,-5,23)
for x in array1:
	if (x%2==0):
		print x
names=("good","very good","excellent")
print names[0]
print names[2]

from numpy import matrix
from numpy import linalg
M= matrix([[1,2,3],[4,5,6],[7,8,9]])
print M
print M.item(4)
