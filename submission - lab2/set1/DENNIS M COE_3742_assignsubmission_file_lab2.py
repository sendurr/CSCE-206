tup1 = ("jimmhy", 98, 35, 56)
tup2 = ("jones", 89, 88, 98)
tup3 = ("lucy", 99, 90, 98)

X = [tup1, tup2, tup3]

print (X[1][3])

M = [[1, 1, 1], [1, 1, 1], [1, 1, 9]]
M1 = [[2, 2, 2], [2, 8, 2], [2, 2, 2]]
M3 = [M, M1]

print M3[0][2][2]
print M3[1][1][1]

jimmys_scores = {"physics":58, "math":98, "english":98}

CityT={"Columbia":68, "Charleston":65, "Miami":82, "Houston":75, "Seattle":41, "Chicago":20, "New York City":30, "Myrtle Beach":55, "Springfield":41, "Denver":22}
 
cities=(CityT.keys())
cities=sorted(cities)
  
import operator
sorted_CityT=sorted(CityT.items(), key=operator.itemgetter(0))
print(sorted_CityT)