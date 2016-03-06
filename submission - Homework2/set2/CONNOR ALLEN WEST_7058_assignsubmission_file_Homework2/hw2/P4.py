a = [1,3,5,7,11]
b = [13,17]
c = a+b
print(c)
#prints a new list "c" with the components of b added to the end of a, creating one new list
b[0]=(-1)
d = [e+1 for e in a]
print(d)
#prints the list "a" with every value increased by 1
d.append(b[0]+1)
d.append(b[-1]+1)
print(d[-2:])
#prints the last two values in the list "d", which was appended to be 0 and 18 in the previous two statements