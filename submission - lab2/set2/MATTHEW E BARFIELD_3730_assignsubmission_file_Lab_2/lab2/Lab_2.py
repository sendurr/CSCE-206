print ("Question 1")
Jimmy = (98, 35, 56)
Jones = (89, 88, 98)
Lucy = (99, 90, 98)
print "Jimmy", Jimmy
print "Jones", Jones
print "Lucy", Lucy
Records = (Jimmy + Jones + Lucy)
print "Jones' 3rd Score:", Records[5]

print ("")

print ("Question 2")
m1 = [[1,1,1], [1,1,1], [1,1,9]]
m2 = [[2,2,2], [2,8,2], [2,2,2]]
m3 = m1 + m2
for row in m3:
	print row
print m3[4][1], m3[2][2]
print ("")

print ("Question 3")
JS = {'Physics': 58, 'Math': 98, 'English': 98}
for Study in JS:
	print Study, "%10.1f"%JS[Study]

#print "Jimmy's Score:", JS
print ("")

print ("Question 4")
CityTemp = {'Denver': 2, 'Aspen': 3, 'Dyrlte': 4, 'Cola': 5, 'Chucktown': 6, 'GVegas': 7, 'Oxford': 8, 'Florence': 9, 'Clemson': 666}
for City in CityTemp:
	print City, "%10.1f"%(CityTemp[City])
print ("")
