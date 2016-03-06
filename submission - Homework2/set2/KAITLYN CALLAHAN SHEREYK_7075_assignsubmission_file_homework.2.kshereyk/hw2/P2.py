import numpy as np 



g=9.81 #global variable
v0=1
n=11
step=(2*v0/g)/(n-1)
for i in range(0,11):
	t=step*i
	y=v0*t-0.5*g*t**2
	print "%f,%f"%(t,y) #print as table





	
	

	


