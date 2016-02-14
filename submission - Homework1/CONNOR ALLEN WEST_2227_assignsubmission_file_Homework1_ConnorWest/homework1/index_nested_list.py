q = [['a','b','c'],['d','e','f'],['g','h']]
print(q)
print(q[0][0])
print(q[1])
print(q[2][1])
print(q[1][0])
print(q[-1][-2])

#This happens because the computer registers the first list as "0", the next "1" and so forth
#So when you input the negatives, the computer registers this as backwards
#So "-1" goes to what is 2 in the lists, and "-2" in the nested list will go to g
