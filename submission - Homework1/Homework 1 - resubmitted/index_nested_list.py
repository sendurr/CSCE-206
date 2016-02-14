from itertools import chain
q= [['a', 'b', 'c'], ['d','e', 'f'], ['g', 'h']]
for i in q:
	for j in range(len(i)):
		print (i[j])

i=0
num = len(q)
while i < num:
	print(q[i])
	i+=1

print (q[0][0])
print(q[1])
print(q[2][1])
print(q[1][0])
print(q[-1][-2])
#the negatives r3epresent the inverse of the fucntion
#-1 means you start in the last row instead of the first
#-2 means you start at the last number first
