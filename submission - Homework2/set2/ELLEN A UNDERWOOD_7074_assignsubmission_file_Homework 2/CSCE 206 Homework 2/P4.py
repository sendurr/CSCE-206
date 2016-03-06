a=[1,3,5,7,11]
b=[13,17]
c=a+b
print c #this prints both of the lists together, adding 13 and 17 to the end of a

b[0]=-1
d=[e+1 for e in a]
print d #this prints all the numbers in a plus 1 each

d.append(b[0]+1)
d.append(b[-1]+1)
print d[-2:] #this prints the last 2 numbers in the d list, which just added -1+1=0 and the last number in b
#17+1=18