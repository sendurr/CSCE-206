import operator

d=[("jimmhy",98,35,56),("jones",89,88,98),("lucy",99,90,98)]
print(d[1][3])

#-------------------------------------------------------------

import numpy as np

x= (np.array([[1,1,1],[1,1,1],[1,1,9]]))
y= (np.array([[2,2,2],[2,8,2],[2,2,2]]))
M3= (x,y)
print(M3)

print(M3[1][1][1])
print(M3[0][-1][-1])

#-------------------------------------------------------
jimmysscore ={"physics": 58, "math":98, "english":98}
print(jimmysscore)

#--------------------------------------------------------

CityT={"Atlanta":60, "NewYork":20, "SanFrancisco": 80, "Spartanburg":45, "Raleigh":75, "Durham":43, "Chapin":25, "Tuscalusa":85, "Cincinati":57, "Chicago":100}

