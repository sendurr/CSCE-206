file1=open("density_water.dat",'r')
file2=open('density_air.dat','r')
water=file1.readlines()
air=file2.readlines()

twater=[]
dwater=[]
tair=[]
dair=[]
skip=0
for x in water:
	for i in range(0,1):
		for j in range(0,1):
			if (j>=0):
				if x=='\n' or x[0]=='#':
					skip+=1
					continue
				try:
					twater.append(str(x.strip().split()))
				except:
					skip+=1
					continue
for x in twater:
	for i in range(0,1):
		for j in range(0,1):
			dwater.append(x.split(','))
for x in air:
	for i in range(0,1):
		for j in range(0,1):
			if(j>=0):
				if x == '\n' or x[0]=='#':
					skip+=1
					continue
for x in tair:
	for i in range(0,1):
		for j in range(0,1):
			dair.append(x.split(','))
print (twater)
print(tair)
print(dwater)
print(dair)