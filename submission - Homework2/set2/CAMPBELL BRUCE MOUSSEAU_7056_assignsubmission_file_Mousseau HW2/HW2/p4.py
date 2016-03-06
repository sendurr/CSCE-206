a = [1,3,5,7,11]
b = [13,17]
c = a+b
print (c)  #variable 'c' is just combining the two lists 'a' and 'b'

b[0] = -1
d = [e+1 for e in a]
print (d) #variable 'd' just increased each number in list 'a' by one using a for loop
#the function in line 6 is affecting the first variable in list 'b', assigning it a new value of -1

d.append(b[0]+1)
d.append(b[-1]+1)
print(d[-2:]) #this function is building off what was started in line 10, appending list 'b' by adding 1 to the first and second variables in the new list 'b'
