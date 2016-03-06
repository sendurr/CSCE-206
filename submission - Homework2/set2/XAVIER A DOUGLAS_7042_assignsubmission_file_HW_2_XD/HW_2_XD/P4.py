
a = [1,3,5,7,11]
b = [13,17]
c = a + b
print(c)
# prints list a and b combined
b[0] = -1
d = [e+1 for e in a]
print(d)
# prints list d which is each number in list a + 1
d.append(b[0] + 1)
d.append(b[-1] + 1)
print(d[-2:])
# prints the last to items in the appended version of d