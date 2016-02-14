#1----------------------------
L1=[2, 3, 4,10]
L2=[5,3,4,9,10,15]

a=set(L1)
b=set(L2)
print(a & b)
print(L1[0])
print(a-b)
L3=a|b
print(L3)
L2.append(103)
L2.append(20)
L2.append(34)
print(L2)
#2--------------------------------------------
total=0
for i in range(13,999):
        if i % 2 == 1:
            total+=i
            print(total)
#3---------------------------------------------
import random
x=[int(300*random.random()) for i in range(300)]
result= list(filter(lambda y: (y%3==0 and y%7==0),x))
print("values factorable by 3 & 7", result)