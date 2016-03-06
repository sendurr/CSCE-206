#2
print "2."
#while loop
s=0
k=1.0
M=25
while k<=M:
	s+=1/k
	k+=1
print s

#for loop
s=0
k=1
M=25
for i in range(k,M+1):
	s+=1.0/i
print s
print 

#3
print "3."
M=[[1,2,3],[4,5,6],[7,8,9]]
print M[0][0]+M[0][1]+M[0][2]+M[1][0]+M[1][2]+M[2][0]+M[2][1]+M[2][2]
