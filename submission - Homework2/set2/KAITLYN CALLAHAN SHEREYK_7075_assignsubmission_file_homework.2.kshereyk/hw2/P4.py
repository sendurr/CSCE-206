a=[1,3,5,7,11]
b=[13,17]
c=a+b
print c #this prints out the merging of both lists into one list

b[0]=-1
d=[e+1 for e in a]
print d # this printed even numbers starting from the first number in the list a and added 1 value to each number in the list

d.append(b[0]+1)
d.append(b[-1]+1)  
print d[-2:] #this prints out 0 because b[0]=-1 so that plus 1is 0. and the last number in b list plus 1 which is 18 and adds to the end of that list giving [0,18]