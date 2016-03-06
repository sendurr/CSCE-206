#Question 4--------------------
a=[1,3,5,7,11]
b=[13,17]
c=a+b
print(c)
#this print statement is the combination of the two lists
b[0]= -1
d = [e+1 for e in a]
print(d)
#this is a list that is all of the numbers in a that have had 1 added to them
d.append(b[0]+1)
d.append(b[-1]+1)
print(d[-2:])
#this is printing the list where b[0] was appended to -1 and then had 1 added 
#AND it is also the list where the last element in b had 1 added to it 
#the print function is acutally printing the last two elements in the appended "b" list
