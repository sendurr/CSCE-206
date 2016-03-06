def area(v):
	answer=(0.5*abs(((v[1][0]*v[2][1])-(v[2][0]*v[1][1])-(v[0][0]*v[2][1])+(v[2][0]*v[0][1])+(v[0][0]*v[1][1])-(v[1][0]*v[0][1]))))
	return answer

vertices=[[0,0],[1,0],[0,2]]
print ("area of triangle=",area(vertices))

