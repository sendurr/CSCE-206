q = [['a','b','c'], ['d','e','f'], ['g','h']]
# extract the letter a
print q[0][0]
# extract the list [d,e,f]
print q[1]
# the last element h
print q[-1][-1]
# the d element
print q[1][0]

#why does q[-1][-2] have the value g
print q[-1][-2]
# this happens because g is in the last list ([-1]) 
# and the second to last letter ([-2])