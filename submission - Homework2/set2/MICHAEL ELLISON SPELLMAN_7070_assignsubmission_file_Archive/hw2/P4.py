a = [1,3,5,7,11]
b = [13,17]
c = a+b
print c
#this prints out all of the numbers from both lists

b[0]=-1
d=[e+1 for e in a]
print d
#This adds 1 to each number in list a

d.append(b[0]+1)
d.append(b[-1]+1)
print d[-2:]
#prints out 0 first because the b[0] = -1 so then it adds 1 so its 0
#prints out 18 because it adds 1 to the last number in list b which is 17
#prints 0 and 18 only beacuse the d[-2:] tells it too