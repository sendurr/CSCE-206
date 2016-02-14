import pprint


t1 = ("jimmhy", 98, 35, 56, "jones", 89, 88, 98, "lucy", 99,90,98)
print t1
print t1[6]

m3 = [['1', '1', '1'], ['1', '1', '1'], ['1', '1', '9'], ['2', '2', '2'], ['2', '8', '2'], ['2', '2', '2']]
for row in m3:
	print ' '.join(row)


print m3[2][2]

print m3[4][1]


jimmyscore = {"Physics":58, "Math":98, "English":98}

print jimmyscore.keys()
print jimmyscore.values()


CityT = {"Denver":70, "Charleston":67, "Houston":87, "Austin":90, "Seattle":55, "Rio":49, "Charlotte":72, "Juneau":16, "Nome":-8, "Redding":115}

cities = sorted(CityT.keys())

for city in cities:
	print city, "\t", CityT[city]


