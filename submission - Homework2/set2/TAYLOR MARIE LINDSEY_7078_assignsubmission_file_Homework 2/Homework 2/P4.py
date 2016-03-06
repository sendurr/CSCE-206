
a=[1,3,5,7,11]
b=[13,17]
c=a+b
print c
#lists a and b are added together

b[0]=-1
d=[e+1 for e in a]
print d
#a new list is made from the first term in b and the last term in a

d.append(b[0]+1)
d.append(b[-1]+1)
print d[-2:]
#two new terms are added to list d 