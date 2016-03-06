r1=-1
r2=1
r3=2
x=15

roots=[r1,r2,r3]
mult=1
for i in roots:
	mult*= (x-i)
print "with roots (-1,1,2)=",mult
