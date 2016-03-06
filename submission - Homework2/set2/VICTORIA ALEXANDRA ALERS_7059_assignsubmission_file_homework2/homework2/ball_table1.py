v0 = 1
g = 9.81
ti=0
tf=((2*v0)/g)
n=0
step=tf/11
print("t\t\ty(t)")
while ti< tf:
	y=(v0-ti)-(0.5*g*(ti**2))
	ti+=step
	print("%f\t%f"%(tf,y))