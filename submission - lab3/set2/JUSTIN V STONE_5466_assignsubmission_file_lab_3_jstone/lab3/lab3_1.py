L1 = {2,3,4,10}
L2 = {5,3,4,9,10,15}

print "In both L1 and L2:", L1 & L2 
print "In either L1 or L2, but not both:", L1^L2
print "In L1 but not in L2:", L1-L2

L3 = L1|L2
print "Merge of L1 and L2 equals L3:", L3

L1 = list(L1)
L2 = list(L2)

L2.append(103)
L2.append(20)
L2.append(34)

print "L2:", L2