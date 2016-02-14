def remove_duplicates():
	L1= [2,3,4,10]
	L2= [5,3,4,9,10,15]
	for L1 in L2:
		L1.append(L1.remove())
	return L1
	print (L1)

L1= [2,3,4,10]
L2= [5,3,4,9,10,15]
L3= [item for item in L1 if item not in L2]
print (L3)

mergedlist = L1 + L2
print (mergedlist)

L2= [5,3,4,9,10,15];
L2.append(103);
L2.append(20);
L2.append(34);
print (L2)