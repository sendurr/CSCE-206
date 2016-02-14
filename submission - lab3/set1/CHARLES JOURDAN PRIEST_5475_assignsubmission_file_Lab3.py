L1={2,3,4,10}
L2={5,3,4,9,10,15}

print (L1&L2)

print (L1^L2)

print (L1-L2)

L3= L1|L2

L2=[5,3,4,9,10,15]
L2.append(103)
L2.append(20)
L2.append(34)
print (L2)


y=0
x=13
while x<= 997:
	y=y+x
	x=x+2

print (y)


import random
x=[int(300*random.random()) for i in range(300)]
i=0

for i in x:
	while i<300:
		if x%3==0:
			print(x)
		if x%7==0:
			print(x)
		i=i+1