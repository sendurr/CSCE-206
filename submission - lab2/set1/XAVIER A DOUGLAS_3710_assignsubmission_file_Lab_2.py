#1
print("#1")
t1 = ("jimmy", 98,35,56)
t2 = ("jones",89,88,98)
t3 = ("lucy",99,90,98)
tlist = [t1,t2,t3]
print("Jones' third subject score =",tlist[1][3])

#2
print("#2")
M3 =[[1,1,1],[1,1,1],[1,1,9],[2,2,2],[2,8,2],[2,2,2]]
print(M3[4][1])
print(M3[2][-1])

#3
print("#3")
d = {"Physics:":58, "Math:":98, "English:":98}
x = (d.keys())
for x in d:
	print(x,"\t",d[x])

#4
print("#4")
CityT = {"Columbia":67, "Midway":71, "Hinesville":69, "San Diego":75, "Duluth":68, "Atlanta":62, "Chicago":21, "Norfolk":19, "Sacremento":63, "Corpus Christie":73}
print("Number of Cities in CityT:",len(CityT))
city = (CityT.keys())
for city in CityT:
	print(city,"\t",CityT[city])
