#Question1
jimmhy = ('98', '35','56')
jones = ('89', '88', '98')
lucy = ('99','90','98')
print(jones[2]) 

#Question2
M1=[(1,1,1), (1,1,1), (1,1,9)]
M2=[(2,2,2),(2,8,2),(2,2,2)]
M3=[M1,M2]

print( M3[0][2][2], M3[1][1][1])

#Question3
dictionary={"physics":58,"math":98, "english":98}
print("Jimmy's score")
for subject in dictionary:
	print(subject, dictionary[subject])


#Question4
CityT={"Columbia":70, "Charleston":67, "Sprinberg":87, "New York City":45, "Tampa Bay":83,"Miami":91,"Los Angeles":79,"Chicago":50, "Dallas":78, "Washington D.C.":56}
print(CityT)