a = [1,3,5,7,11]
b = [13,17]
c = a+b
print c
'''addition of lists appends the values of the two lists
into a new list, so printing the addition of
[1,3,5,7,11] + [13,17] would yield c = [1,3,5,7,11,13,17]
'''

b[0] = -1
d = [e+1 for e in a]
print d
'''a for loop is run over the values stored in a and 1 is added
to each value, then stored into d. d will equal
[1+1,3+1,5+1,7+1,11+1] = [2,4,6,8,12]'''

d.append(b[0]+1)
d.append(b[-1] + 1)
print d[-2:]

'''previous statement b[0] = -1 means current b = [-1,17]
values are being appended onto d = [2,4,6,8,12].
first appended value is b[0]+1, b[0] = -1, so value = 0.
next appended value is b[-1] = last value of b = 17. 17+1 = 18
new d will equal [2,4,6,8,12, 0, 18], but the print is only being
to print the second to last through the last item (the newly appended
items)  [0,18]
'''