jimmhy= (98,35,56)
jones= (89,88,98)
lucy=(99,90,98)
print (jones[2])

M3 = [[[1 for col in range(3)]for row in range(3)] for x in range(3)] +[[[2 for col in range(3)]for row in range(3)] for x in range(3)]
M3[2][2][2]  = 9
M3[4][1][1]  = 8 
print (M3[2][2][2])
print (M3[4][1][1])

print ("jimmy's score")
dictionary={"physics":58, "math":98, "english":98}
print (dictionary)

temp = {"Columbia":70, "Charleston":67, "Sprinberg":87, "Dallas":90, "Memphis":20, "Atlanta":64, "Austin":22, "El Paso":59, "Miami":85, "Seattle":12}
cities=(temp.keys())
cities=sorted(cities)
for city in cities:
	print (city, "\t",temp[city])