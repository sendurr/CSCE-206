a=[1,3,5,7,11]
b=[13,17]
c=a+b
print c,"In this print statement, list a is added to list b, making a list containing all of the values of 'a' and 'b' in it."
print " "
b[0]=-1
d=[e+1 for e in a]
print d,"In this print statement, 1 is added to each value  that is contained in list 'a', and each new value is put into list 'd'."
print " "
d.append(b[0]+1)
d.append(b[-1]+1)
print d[-2:],"In this print statement, list 'd' is appended by adding b[0]+1 = (-1+1=0) and b[-1]+1 = (17+1=18) to the end of the list. The last two elements of the newly appended list 'd' is all that is listed."