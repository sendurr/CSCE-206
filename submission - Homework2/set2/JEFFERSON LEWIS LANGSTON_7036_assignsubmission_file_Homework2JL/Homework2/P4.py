a = [1,3,5,7,11]
b = [13,17]
c = a + b
print c
#Here lists a and b are being combined and printed into a single list.
b[0] = -1
d = [e+1 for e in a]
print d
#Variable d is increasing the numbers in list a by a single integer. However, the command in line 6 makes the first value of list b -1.
d.append(b[0]+1)
d.append(b[-1]+1)
print d[-2:]
#This is a continuation of what was done previously, making the values of list d become 0 and 18 by turning the first value of list b to -1 and adding 1, and adding one to the second value of list b making it 18.



