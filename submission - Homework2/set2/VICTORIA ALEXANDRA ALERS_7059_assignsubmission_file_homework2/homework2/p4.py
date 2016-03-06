a=[1,3,5,7,11]
b=[13,17]
c=a+b
print(c)
#this opperation allows a person to combine two lists into one
b[0]=-1
d=[e+1 for e in a]
print (d)
#the operation allows the user to increase all values in the list by one
d.append(b[0]+1)
d.append(b[-1]+1)
print(d[-2:])
#the first opperation changes the index of b[0] that was originally changed to -1 and adds 1
#causing the new value to be 0
#the second opperation changed the last value in the list b to go up by one making it 18.
#both opperations add these new values to list d 
#the print is asking for the last two values in list d which is the two new values that were just appended into the list