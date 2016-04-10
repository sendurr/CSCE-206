import numpy as np
import matplotlib.pyplot as plt
def read_file(mydata):
	mydata=str(mydata)
	infile=open(mydata,"r")
	data={"temprature":[],"density":[]}
	
	for x in infile:
		if x=="\n" or x[0]=="#":
			continue
		else:
			items=x.split()
			data["temprature"].append(float(items[0]))
			data["density"].append(float(items[1]))
	data["temprature"]=np.array(data["temprature"])
	data["density"]=np.array(data["density"])
	infile.close
	return data
def fit(x,y,variable):
	coeff1=np.polyfit(x,y,1)
	coeff2=np.polyfit(x,y,2)
	p1=np.poly1d(coeff1)
	p2=np.poly1d(coeff2)
	plt.plot(x,y,"bo")
	plt.plot(x,p1(x))
	plt.plot(x,p2(x))
	plt.axis=(x[0]+5,x[-1]+5,min(y)-0.05,max(y)+0.5)
	plt.xlabel("temprature")
	plt.ylabel("density")
	plt.legend(["t^2*exp(-t^2)", "t^4*exp(-t^2)"])
	plt.title("the relationship between density and temprature of %s)"%(variable))
	plt.legend(['data','degree1','degree2'])
	plt.show()

data=read_file("density_air.dat")
fit(data["temprature"],data["density"],"air")

data=read_file("density_water.dat")
fit(data["temprature"],data["density"],"water")

