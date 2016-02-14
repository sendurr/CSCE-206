#Homework 1,Exercise 4 by John Welsh

q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]

part_1 = q[0][0]
part_2 = q[1]
part_3 = q[-1][-1]
part_4 = q[1][0]

print "1. %s\n2. %s\n3. %s\n4. %s" % (part_1, part_2, part_3, part_4)
print "\nq[-1][-2] has the value of g because the first index, [-1], references the\
 final element in the top level loop: %s. Then, the second index, [-2], references\
 the second to last index in that element: %s." %(q[-1], q[-1][-2])