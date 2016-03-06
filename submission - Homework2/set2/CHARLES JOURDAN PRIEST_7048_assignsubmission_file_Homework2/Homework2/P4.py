a=[1,3,5,7,11]
b=[13,17]
c=a+b
print (c)
# this print statement adds the 2 values in list b to the end of list a, creating list c
b[0]=-1
d=[e+1 for e in a]
print (d)
# this list is a modified version of list a, where every value is increased by 1
d.append(b[0]+1)
d.append(b[-1]+1)
print (d[-2:])
# this print statement prints a modified list of d including only the last two values in the list, 0 and 18, which were added to the list after the second print statement