a=[1,3,5,7,11]
b=[13,17]
c=a+b

print(c)
#list a and b were added to eachother.

b[0]=-1
d=[e+1 for e in a]

print(d)
#from list a we printed list e which adds 1 to each number in list a

d.append(b[0]+1)
#d.append(b[-1]+1)
print(d[-2:])
#from list b first index add 1 then from list b last index add 1