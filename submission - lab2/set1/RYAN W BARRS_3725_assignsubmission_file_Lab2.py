#1
T = [("jimmhy",98, 35, 56),("jones",89, 88, 98),("lucy",99, 90, 98)]
print T[1][3]

#2
M = [[1,1,1],[1,1,1],[1,1,9]]
M1 = [[2,2,2],[2,8,2],[2,2,2]]
M3 = [M,M1]
print M3[0][2][2], M3[1][1][1]

#3
scores = {"physics":58, "math":98, "english":98}
print "Jimmy's score"
for subject in scores:
	print subject, scores[subject]

#4
CityT = {"Berkeley": 48, "Fairfield": 49, "Fremont":50, "Sacramento":74, "San Francisco": 64, "San Jose": 71, "Long Beach": 75, "Los Angeles": 72, "Pasadena": 79, "San Diego": 70}
print CityT