#tuple
t1=("jimmy",98,35.56)
t2=("jones",89,88,98)
t3=("lucy",99,90,98)
print t2[3]

#matrix

M3=[[1,1,1],[1,1,1],[1,1,9],[2,2,2],[2,8,2],[2,2,2]]
print "sum matrix**********"
total=0
for x in M3:
	print x
print M3[2][2]
print M3[4][1]

#dicionaries
jimmyscores={"Physics":58,"Math":98,"English":98}
print jimmyscores

CityT={"Chicago":20,"Columbia":60,"Charleston":65,"Fort Myers":80,"Nashville":50,"Boulder":35,"San Diego":75,"Las Vegas":75,"Madison":45,"New Orleans":72}
print CityT
cities= sorted(CityT.keys())
print cities
for city in cities:
	print city,"\t",CityT[city]
