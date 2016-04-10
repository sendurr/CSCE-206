infile=open("density_water.dat","r")
infile1=open("density_air.dat","r")
water=infile.readlines()
air=infile1.readlines()

water_temp=[]
water_density=[]
air_temp=[]
air_density=[]
skips=0
for x in water:
	for i in range(0,1):
		for j in range(0,1):
			if (j>=0):
				if x=="\n" or x[0]=="#":
					skips+=1
					continue
				try:
					water_temp.append(str(x.strip().split( )))
				except:
					skips +=1
					continue
for x in water_temp:
	for i in range(0,1):
		for j in range(0,1):
			water_density.append(x.split(","))
for x in air:
	for i in range(0,1):
		for j in range(0,1):
			if (j>=0):
				if x=="\n" or x[0]=="#":
					skips+=1
					continue
				try:
					air_temp.append(str(x.strip().split( )))
				except:
					skips +=1
					continue
for x in air_temp:
	for i in range(0,1):
		for j in range(0,1):
			air_density.append(x.split(","))
print water_temp
print air_temp
print water_density
print air_density