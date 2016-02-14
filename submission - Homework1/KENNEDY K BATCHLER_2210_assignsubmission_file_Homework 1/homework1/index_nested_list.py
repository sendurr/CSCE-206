q=[['a','b','c'],['d','e','f'], ['g','h']]
print (q[0][0])
print (q[1])
print (q[2][1])
print (q[1][0])

print "Answer: q[-1][-2] has the value g because the starting value [0][0] is the first set, starting at a. going backwards (-1) would put you at the third set. from there, you would have to go back 3 from a. therefore [-1][0] would be undefined as there is no [0] value. [-1][-1] would give you h. Finally, [-1][-2] would give you g"