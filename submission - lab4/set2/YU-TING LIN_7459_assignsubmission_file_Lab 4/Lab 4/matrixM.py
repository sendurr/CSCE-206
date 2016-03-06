M= [[1,2,3],[4,5,6],[7,8,9]]
N= [[1,1,1],[1,1,1],[1,1,1]]
print M

for i in range(len(M)):
 for j in range(len(N[0])):
  for k in range(len(N)):
       result[i][j] += M[i][k]*N[k][j]
 
for r in result:
   print(r)

