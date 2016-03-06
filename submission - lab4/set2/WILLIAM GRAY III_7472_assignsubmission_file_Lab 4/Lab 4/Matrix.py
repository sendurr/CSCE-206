import numpy

M=numpy.zeros((3,3))
M[0]=[1,2,3]
M[1]=[4,5,6]
M[2]=[7,8,9]

s=[]
for x in range(0,3):
	value1=M[x,0]
	value2=M[x,-1]
	value3=value1+value2
	s.append(value3)
	
print(s)
print("outer_sum=",sum(s))

