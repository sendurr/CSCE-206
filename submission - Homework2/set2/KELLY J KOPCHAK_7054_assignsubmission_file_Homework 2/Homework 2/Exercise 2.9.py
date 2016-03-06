a=[1,3,5,7,11]
b=[13,17]
c=a+b
print c #print both lists a and b combined into one list, c
b[0]=-1
d=[e+1 for e in a]
print d #print the list d that is adding 1 to each value in list a
d.append(b[0]+1) #added 0 to the end of list d, becuase b[0]=-1 
d.append(b[-1]+1)#added 1 to b[-1] which is 17, so yeilds 18
print d[-2:]#print the value in the second index to the left of the 0th index of the newly appended d and each subsequent value to the end of the list