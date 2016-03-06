a = [1, 3, 5, 7, 11]
b = [13, 17]
c = a + b
print c
print ""
b[0] = -1
d = [e+1 for e in a]
print d
print ""
d.append(b[0] + 1)
d.append(b[-1] + 1)
print d[-2:]

#the first print statements prints the combined lists
#the second print statement prints list d, which is list a +1 at each value
#the third print statement prints the revised list d, which has been altered several times, the first changed the 13 to -1, then this was appended to be 0 in the third to last command, then the 17 was changed to an 18 in the other append command