a=[1,3,5,7,11]
b=[13,17]
c=a+b
print c  #prints lists a and b combined into one list
# would print [1,3,5,7,11,13,17]

b[0]=-1  #changes the value 13 in list b to -1
d=[e+1 for e in a]
print d  #prints the sum of one and every value in list a
# would print [2,4,6,8,12]

d.append(b[0]+1)
d.append(b[-1]+1)
print d[-2:]  #prints list d from the second to last element to the end of the list (last two elements) after changes are made to list d
# would print [0,18] 