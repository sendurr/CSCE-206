#X'Avier Douglas - HW 1
#Exercise 2.19

q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g','h']]
print("1 =", q[0][0])
print("2 =", q[1])
print("3 =", q[2][-1])
print("4 =", q[1][0])

#Explain
#q[-1][-2] prints "g" because the 
#"-" tells python to look at the
#list from right to left instead of
#left to right as usual and "g" is
#in the first list from the right
#and it is the second element of the
#list from the right.