#jones' third subject score
t1=("jimmy",98,35,56)
t2=("jones",89,88,98)
t3=("lucy",99,90,98)

print "jones' third score=", t2[3]

#matrix
M3=([1,1,1],[1,1,1],[1,1,9],[2,2,2],[2,8,2],[2,2,2])
print M3[2][2]
print M3[4][1]

#dictionary
jimmyscores={'physics':58,'math':98,'english':98}
print "jimmy's scores:", jimmyscores

#temperature of cities
CityT={'Chicago':32, 'Boston':40, 'New York':42, 'San Francisco':65, 'San Diego':81, 'Miami':89, 'Columbia':78, 'Philadelphia':50, 'Denver':57, 'Portland':66}
cities= CityT.keys()
cities= sorted(cities)
for city in cities:
	print city, "\t", CityT[city]