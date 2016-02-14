L1l=[2, 3, 4,10]
L2l=[5,3,4,9,10,15]
L1s={2, 3, 4,10}
L2s={5,3,4,9,10,15}

print "exists in both:", L1s & L2s
print "exists in both:",L1l[1],L2l[2],L1l[3]
print "in L1 and not in L2:", L1s | L2s

L3 = L1l+L2l
print "L3:",L3

L2l.append(103),L2l.append(20),L2l.append(34);
print "appended L2:", L2l