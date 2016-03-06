#simulate operations on lists by hand:
#explain what is printed by each print statement

a= [1,3,5,7,11]
b= [13,17]
c = a+b
print c
 #This prints out a list with both a and b added together
b[0] = -1
d = [e+1 for e in a]
print d 
#This prints out the list a with a 
#for loop that adds 1 to every value in the original a list and saves it 
#as a new list d
d.append(b[0]+1)
d.append(b[-1]+1)
print d[-2:] #this prints out the last two numbers of the new list d after b[0] was
#added to the list. The d.append commands added 1 to those numbers to make them 
#go from -1 to 0 and last number 17 to 18 