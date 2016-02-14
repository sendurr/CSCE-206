q = [['a','b','c'],['d','e','f'],['g','h',]]

print q[0][0]
#calls the top right

print q[1]
#calls the middle row

print q[2][1]
#calls the second column of the third row

print q[-1][-2]
print("This calls [2][0] because it goes one left from the first place which would then call the equivalent of [2].  Then it travels two left of the g, which would call g also.")
#ends the code