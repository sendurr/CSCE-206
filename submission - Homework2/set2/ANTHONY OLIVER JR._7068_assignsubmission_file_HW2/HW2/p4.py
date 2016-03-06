a = [1, 3, 5, 7, 11]
b = [13, 17]
c = a + b
print (c) # adds up both lists into 1 singular list
b[0] = -1
d = [e+1 for e in a]
print (d) #adds +1 to all intervals in the list a
d.append(b[0] + 1)
d.append(b[-1] + 1)
print (d[-2:]) # prints the last two items in list b
#which happens to be the only two items in list b
#with the proper appends according to the d.append commands