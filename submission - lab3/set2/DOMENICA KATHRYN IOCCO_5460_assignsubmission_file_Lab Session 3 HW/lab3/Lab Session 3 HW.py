#play with list and set
L1=set([2,3,4,10])
L2=set([5,3,4,9,10,15])
set(L1) & set(L2)
#numbers that exist in both L1 and L2
print("intersection:", L1 & L2)
#in either L1 or L2 but not both
print(L1 ^ L2)
#numbers in L1 but not L2
print(L1-L2)
#merge L1 and L2
L3 = ("union:", L1 | L2)
print(L3)
#add 103, 20, and 34 to L2
L2 = [5,3,4,9,10,15];
L2.append(103);
print("Updated list:", L2)
L2.append(20);
print("updated list:", L2)
L2.append(34);
print("updated list:", L2)

#loop application
Newlist = []
for x in range(13,999,2):
	Newlist.append(x)
	#print(Newlist)
	print(sum(Newlist))

#random integers code
import random
x = [int(300*random.random()) for i in range(300)]
print(x)
result = list(filter(lambda z: (z%7==0 and z%3==0), x))
print("Numbers divisible by 7 and 3 are", result)
	