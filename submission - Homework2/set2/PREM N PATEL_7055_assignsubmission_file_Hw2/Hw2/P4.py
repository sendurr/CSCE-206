a = [1,3,5,7,11]
b = [13,17]
c = a + b
print c  # print new list c, including all numbers in list a and list b

b[0] = -1
d = [e+1 for e in a]
print d   # print list d, just adding 1 to all the numbers in list a

d.append(b[0] +1)
d.append(b[-1]+1)
print d[-2:]
# print the last to numbers in list d, after adding the numbers 0 and 18 to the end of the list