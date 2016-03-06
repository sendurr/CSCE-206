#given n+1 roots r0, r1,...,rn of a polynomial p(x) of 

n = 15
R1 = -1
R2 = 1
R3 = 2
ListofRoots = [R1, R2, R3]

poly = 1
for i in ListofRoots:
    poly *= (n - i)

print poly
