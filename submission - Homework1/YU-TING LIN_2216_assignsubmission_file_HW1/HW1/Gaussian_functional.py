import math
m= 00.0
s= 2.0
x= 1.0
#f(x)= 1/(2*math.pi)*s*math.exp(-0.5(x-m/s)**2)
#print f(x)


a= (-0.5)*(((x-m)/s)**2.0)
print a

b= math.sqrt(2*(math.pi)) * s

c= 1.0 /b

result = c * math.exp(a)
print result