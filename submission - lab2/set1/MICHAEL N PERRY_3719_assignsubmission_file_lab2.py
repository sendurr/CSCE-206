print "Question 1"
tup1=("jimmhy",98,35,56)
tup2=("jones",89,88,98)
tup3=("lucy",99,90,98)
print tup2[3]
print " "

print "question 2"
M3=[
[[1,1,1],
[1,1,1],
[1,1,9]],

[[2,2,2],
[2,8,2],
[2,2,2]]
]
print M3[0][2][2],",",M3[1][1][1]
print " "

print "question 3"
print "jimmy's score"
js={"physics:":58,"math:":98,"english:":98}
for subject in js:
	print subject,js[subject]
print " "

print "question 4"
cityT={"Boston":55,"New York":60,"Los Angeles":70,"San Diego":72,"Columbia":60,"Asheville":54,"Atlanta":61,"Austin":68,"Baltimore":53,"Denver":47}
for cities in cityT:
	print cities,cityT[cities]