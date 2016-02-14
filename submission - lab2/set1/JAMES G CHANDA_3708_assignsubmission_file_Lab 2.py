#1) Store the following student records into a variable using list of tuples
print "****Question 1****"
Jimmhy = (98, 35, 56)
Jones = (89, 88, 98)
Lucy = (99, 90, 98)
print "Jimmhy:", Jimmhy
print "Jones:", Jones
print "Lucy:", Lucy
Var = (Jimmhy + Jones + Lucy)
print "Jones' 3rd score:", Var[5]


#2) Create a 3 dimension matrix of 3x3x3 and store it into M3 variable the values are
print "****Question 2****"
M1 = [[1,1,1],[1,1,1],[1,1,9]]
M2 = [[2,2,2],[2,8,2],[2,2,2]]
M3 = M1+M2
for line in M3:
	print line
print M3[2][2], M3[4][1]


#3) Store student subject score for a student into a variable of dictionary
print "****Question 3****"
print "Jimmy's score"
Jimmy = {"Physics:": 58, "Math:": 98, "English:": 98}
for subject in Jimmy:
	print subject,Jimmy[subject]


#4) Store temperature of 10 cities into a variable CityT. Specify your own city names.
print "****Question 4****"
CityT = {"Columbia:": 75, "Athens:": 52, "Paris:": 88, "Madrid:": 66, "New London:": 48, "Berlin:": 32, "Honalulu:": 84, "Liverpool:": 36, "Perth:": 90, "Long Valley:": 27}
print CityT