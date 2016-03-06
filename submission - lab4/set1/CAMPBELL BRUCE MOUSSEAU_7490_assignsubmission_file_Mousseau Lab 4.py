#1
list1=[2,3,5,7,11,13]
for x in list1:
	print (x)
p=17
list1.append(p)
print(list1)

#2
s=0
M=3
k=1
for z in range(k,M+1):
	s=s+(1.0/z)
print (s)

s=0
M=10
k=1
while k<=M:
	s+=(1.0/k)
	k=k+2
	print(s)

#3

M0=[[1,2,3],[4,5,6],[7,8,9]]
print (M0)
sum=0
for c in range(len(M0)):
	for d in range(len(M0[c])):
		if c==0 or c==2 or d==0 or d==2:
			sum+=M0[c][d]
			print(sum)
