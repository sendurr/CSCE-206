q = [['a','b','c'],['d','e','f'],['g','h']]
print ('1)',q[0][0])
print ('2)',q[1])
print ('3)',q[-1][-1])
print ('4)',q[1][0])
#q[-1][-2] has the value g because using the - in the index goes from the back.
#The [-1] index refers to the ['g','h'] list.
#The [-2] index refers to the g element within that list.