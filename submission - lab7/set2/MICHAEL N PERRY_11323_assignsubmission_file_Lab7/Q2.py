#Q2
import sys
Input=sys.argv[1]
while True:
	try:
		T=open(Input,'r')
		T.close()
		break
	except:
		Input=raw_input("error not a file, try again: ")
File=open(Input,'r')
John=[]
Jimmy=[]
Joseph=[]
Linda=[]
Lilly=[]
for x in File:
	y = x.lower().strip().split(", ")
	for z in y:
		if z=="john":
			John.append(1)
		elif z=="jimmy":
			Jimmy.append(1)
		elif z=="linda":
			Linda.append(1)
		elif z=="lilly":
			Lilly.append(1)
		elif z=="joseph":
			Joseph.append(1)

print "%s %5d"%("John",sum(John))
print "%s %4d"%("Jimmy",sum(Jimmy))
print "%s %3d"%("Joseph",sum(Joseph))
print "%s %4d"%("Linda",sum(Linda))
print "%s %4d"%("Lilly",sum(Lilly))