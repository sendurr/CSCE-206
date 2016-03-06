from math import* 
phip=(1.0+sqrt(5.0))/2.0
phin=(1.0-sqrt(5))/2.0
c=0
stepsize=1
while c<1001:
	F=(phip**c-(phin)**c)/sqrt(5.0)
	print c,F
	c+=stepsize

