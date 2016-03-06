#Question 3--------------------
x=1
h=0.01
xcoordinate= []
for i in range(0,100): #100 only gets to 1.99; 101 gets to exactly 2
	xi = i*h
	xcoordinate.append(x + xi)
print(xcoordinate)