r1=-1
r2=1
r3=2
x=15
roots=[r1, r2, r3]

prod=1
for i in roots:
    prod *= (x - i)

print (prod)
