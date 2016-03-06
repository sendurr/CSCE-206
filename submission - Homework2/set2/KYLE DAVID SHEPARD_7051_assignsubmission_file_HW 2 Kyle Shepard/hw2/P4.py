a=[1,3,5,7,11]
b=[13,17]
c=a+b
print c
#this combines the elements in both a and b into one list

b[0]=-1
d=[e+1 for e in a]
print d
#adds 1 to each element in list a

d.append(b[0]+1)
d.append(b[-1]+1)
print d[-2:]
#this adds 1 to the first and last indexes, and the print[-2:] prints them both