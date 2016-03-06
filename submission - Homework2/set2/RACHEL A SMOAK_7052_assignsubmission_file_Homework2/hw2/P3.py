#Rachel Smoak
#Homework 2
#14 February 2016

#Problem 3
h = 0.01 #Given value
xlist = [] #Empty list to add values to
for i in range(0,101): #Numbers 0 to 100
	x = 1 + i*h #Generate the coordinates
	y = round(x,2) #Round to two decimals to get rid of the long trailing numbers
	xlist.append(y) #Add rounded number to list
print xlist