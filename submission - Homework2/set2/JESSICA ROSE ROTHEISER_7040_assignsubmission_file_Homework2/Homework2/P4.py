a= [1,3,5,7,11]
b=[13,17]
c=a+b
print c
#print c prints the union of list a and list b, 
#or all the items in both lists
b[0]=-1
d= [e+1 for e in a]
print d
#print d prints list a adjusted to be the numbers in list a plus 1
d.append(b[0]+1)
d.append(b[-1]+1)
print d[-2:]
#print d[-2:] prints the last 2 items in list d, which as the two
#lines above show, these values are b[0]+1 which equals 0 and
#b[-1]+1 which equals the last digit in list b, 17, plus 1 which
#equals 18, thus the printed list of [0,18]
