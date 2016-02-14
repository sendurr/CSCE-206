from math import e, sqrt, pi

m=0
s=2
x=1

gauss= (1/(sqrt(2*pi)*s))*e**(-0.5*(float(x-m)/s)**2)
print(gauss)
