a=[1,3,5,7,11]
b=[13,17]
c=a+b
print "two lists are added together to form one list", c 
b[0] = -1
d = [e+1 for e in a] #adds one to each number in a
print "adds one to each number in list a", d
d.append(b[0]+1)  #adds one to the first index in b
d.append(b[-1]+1)
print "prints last two numbers from appended list",d[-2:]  