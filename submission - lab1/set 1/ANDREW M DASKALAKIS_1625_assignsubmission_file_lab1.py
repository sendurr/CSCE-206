from numpy import matrix
#
# Number 1
#

w = 2.33
x = -2
y = "32233"
z = 'I am a boy'

print w
print x
print y
print z

#
# Number 2
#

array1 = [3,4.0,34,-5,23]

for index in range(0,len(array1)):
	if index%2 == 0:
		print array1[index]


#
# Number 3
#

array2 = ["good","very good","excellent"]
print array2[0]
print array2[len(array2)-1]

#
# Number 4
#

m = matrix([[1,2,3],[4,5,6],[7,8,9]])

print m