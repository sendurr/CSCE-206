#Ex 2.19: Index nested list

q = [["a", "b", "c"], ["d", "e", "f"], ["g", "h"]]

#1) extract the letter a:
print "1)", q[0][0]

#2) extract the list ['d', 'e', 'f']:
print  "2)", q[1]

#3) the last element h:
print "3)", q[2][1]

#4) the d element:
print "4)", q[1][0]

#5) explain why q [-1][-2] has the value g
print "5)", q[-1][-2], "python reads the matrix backwards from the negatives which is why value = g"
