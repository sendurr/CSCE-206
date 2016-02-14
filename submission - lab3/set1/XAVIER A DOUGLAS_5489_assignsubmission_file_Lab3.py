
#1
print("#1")
L1 = {2,3,4,10}
L2 = {5,3,4,9,10,15}

print ("intersection:",L1 & L2)
print ("either but in both:",L1-L2 | L2-L1)
print ( "in l1 and not in l2:", L1-L2)

L3 = [L1 | L2]
print("Orginal L3 :",L3)

L3.append(103)
L3.append(20)
L3.append(34)
print("Appended L3 :",L3)


#249964
#2
print("#2")
odd = []
numbers= range(13,1000)
for x in numbers:
	if x%2!=0:
		odd.append(x)
total = sum(odd)
print("total =", total)


#3
print("#3")
import random
x=[int(300*random.random()) for i in range(300)]
numbers= range(100)
for x in numbers:
	if x%3==0 and x%7==0:
		print(x)

