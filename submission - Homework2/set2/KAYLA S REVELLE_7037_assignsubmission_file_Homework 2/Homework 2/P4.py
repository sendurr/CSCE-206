
a = [1,3,5,7,11]
b=[13,17]
c=a+b
print("All of the numbers in list a and b is print c:", c)
b[0]=-1
d=[e+1 for e in a]
print("Print d is each number in list a plus 1:" , d)
d.append(b[0]+1)
d.append(b[-1]+1)
print("Print d[-2:] is 0 because we redefined 13 as -1 and added 1 and then appended 17 to be 18 then printed both numbers:" , d[-2:])