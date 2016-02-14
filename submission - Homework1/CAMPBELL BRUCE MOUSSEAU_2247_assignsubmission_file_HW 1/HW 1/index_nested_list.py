q = [['a','b','c'],['d','e','f'],['g','h']]
print (q[0][0])
print (q[1])
print (q[2][1])
print (q[1][0])
print (q[-1][-2])

#[-1][-2] provides the answer "g" because negative indices count from the right while
# positive indicies count from the left, [-1][-2]=[2][1]