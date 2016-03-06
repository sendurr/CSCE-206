a = [1,3,5,7,11]
b = [13,17]
c = a + b
print c
#Lists a and b are being added together to create a combined List c.
#Therefore, [1,3,5,7,11] from List a and [13,17] from List b are joined.
#This outputs [1,3,5,7,11].

b[0] = -1
d = [e+1 for e in a]
print d
#A value of 1 is being added to each number contained in List a.
#The print function generates a list via a for loop. 
#This creates a list that adds 1 to each value in List a.
#Therefore, [2,4,6,8,12] is printed.

d.append(b[0] + 1)
d.append(b[-1] + 1)
print d[-2:]
#b[0]=-1 defines the first index of List b as -1.
#The append functions add 1 to each of the given indices, outputting 0 and 18.
#This leaves the following list: [-1,13,17,0,18].
#Printing index -2 outputs 0, and ":" indicates to print to the end of the list.
#Therefore, [0,18] is printed.