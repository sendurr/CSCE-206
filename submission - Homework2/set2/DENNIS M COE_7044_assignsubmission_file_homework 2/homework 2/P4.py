a = [1, 3, 5, 7, 11]
b = [13, 17]
c = a + b
print c
b[0] = -1
d = [e + 1 for e in a]
print d
d.append(b[0] + 1)
d.append(b[-1] + 1)
print d[-2:]

#print c is adding a and b into one and printing it out.

#print d is printing out a 1 added to every part of the list.

#print d[-2:] is using the appendices to change the values of the list. b[0]=1 so plus 1 = 0.
#and then b[-1] = 17 + 1 = 18 which is what is printed out [0,18]