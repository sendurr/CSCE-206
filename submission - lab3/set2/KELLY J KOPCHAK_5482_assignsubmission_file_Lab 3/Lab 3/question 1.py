L1={2,3,4,10}
L2={5,3,4,9,10,15}
Set1=L1
Set2=L2
print L1, L2
print (L1|L2)-(L1&L2)
print L1-L2
L3=set(L1).union(set(L2))
print L3

L2=[5,3,4,9,10,15]
L2.append(103)
L2.append(20)
L2.append(34)
print L2