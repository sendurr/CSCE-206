from math import sqrt, pi, exp

m = 0
s = float(2)
x = 1

def f(m,s,x):
    answer = (1/(sqrt(2*pi)*s))*exp(-0.5*(((x - m)/s)**2))
    return answer

print f(m,s,x)