
L1 = {2,3,4,10}
L2={5,3,4,9,10,15}
print (L1 & L2)
print (L1|L2)
print (L1-L2)

list_L1 = list(L1)
list_L2 = list(L2)
L3 = list_L1 + list_L2
print (L3)

list_L2 = list(L2)
list_L2.append(103)
list_L2.append(20)
list_L2.append(34)
print(list_L2)