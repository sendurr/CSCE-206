a=[1,3,5,7,11]
b=[13,17]
c=a+b
print c
# line 4 prints the results of adding the values in set b to the end of set a
b[0]=-1
d=[e+1 for e in a]
print d
# line 8 prints the results of adding 1 to each value in set a
d.append(b[0]+1)
d.append(b[-1]+1)
print d[-2:]
# line 10 changes the first value in b to 12
# line 11 changed the second value in b to 18
# line 12 prints the new set that is a result of the changed made by lines 11 and 12