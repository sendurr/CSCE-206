#1
print ("1.")
t=("jimmhy",98,35,56),("jones",89,88,98),("lucy",99,90,98)
#list of tuples. tuples use parentheses
print("Jones' third subject score:",t[1][-1])
print ()

#2
print ("2.")
M3=[[1,1,1],[1,1,1],[1,1,9]],[[2,2,2],[2,8,2],[2,2,2]]
print (M3[1][-2][-2],',',M3[0][2][2])
print ()

#3
print ("3.")
dictionary={"physics":58,"math":98,"english":98}
print ("jimmy's score:",dictionary)
print ()

#4
print ("4.")
cityT={"Baltimore":51,"Las Vegas":58,"Boise":29,"New Orleans":73,
"Paris":56,"Rome":54,"San Sebastian":57,"Dublin":54,"London":55,
"San Diego":60}
cities=(cityT.keys())
cities=sorted(cities)
for city in cities:
	print (city,"\t",cityT[city])

