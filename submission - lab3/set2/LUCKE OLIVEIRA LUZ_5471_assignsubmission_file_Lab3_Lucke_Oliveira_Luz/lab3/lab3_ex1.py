# Name: Lucke Oliveira Luz		Assignment: Lab 3      Exercise: 1

L1 = [2,3,4,10]
L2 = [5,3,4,9,10,15]
S1 = set (L1)
S2 = set (L2)
print "IN BOTH L1 AND L2 =", S1 & S2
print "IN L1 OR IN L2 EXCLUSIVELY =", (S1 - S2) | (S2 - S1)
print "IN L1 NOT IN L2 =", S1 - S2

S3 = S1 | S2
L3 = list(S3)
print "L3 =", L3

L2.append(103)
L2.append(20)
L2.append(34)
print "NEW L2 =", L2