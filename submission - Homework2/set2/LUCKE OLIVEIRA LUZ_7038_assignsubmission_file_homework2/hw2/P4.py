# Name: Lucke Oliveira Luz			Assignment: Homework 2       Exercise: 4

# I USED COMMENTS IN EACH LINE WITH PRINT COMMANDS TO EXPLAIN

a = [1, 3, 5, 7, 11]
b = [13, 17]
c = a + b
print c # THIS COMMAND PRINTS LIST c FORMED BY LIST b ADDED TO LIST a, WHERE THE ELEMENTS OF LIST b WERE ADDED TO THE END OF LIST a.
b[0] = -1
d = [e+1 for e in a]
print d # THIS COMMAND PRINTS LIST d WHICH CONSISTS OF THE ELEMENTS IN LIST a PLUS 1.
d.append(b[0] + 1)
d.append(b[-1] + 1)
print d[-2:] # THIS COMMAND PRINTS THE LAST TWO ELEMENTS IN LIST d WHICH ARE, RESPECTIVELY, THE FIRST ELEMENT IN b PLUS 1 AND THE LAST ELEMENT IN b PLUS 1.