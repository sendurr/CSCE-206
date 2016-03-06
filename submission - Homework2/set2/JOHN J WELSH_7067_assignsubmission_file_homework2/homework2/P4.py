a = [1, 3, 5, 7, 11]
b = [13, 17]
c = a + b
print c
b[0] = -1
d = [e+1 for e in a]
print d
d.append(b[0] + 1)
d.append(b[-1] + 1)
print d[-2:]

print """ The first print statement will print the combination of lists a and b resulting in the list
[1, 3, 5, 7, 11, 13, 17].
The second print statement will print list d which is the result of adding 1 to each element in list a; therefore it will print [2, 4, 6, 8, 12].
The third print statement will print the last two elements of the d list after it has been appended with values 1 greater than the first and last elements of list b.
The first element in list b, however, is first changed to -1. Therefore, the third print statement prints [0, 18]"""