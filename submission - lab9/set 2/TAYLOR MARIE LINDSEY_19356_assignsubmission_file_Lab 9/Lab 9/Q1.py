
from F import F
from math import sin, exp

f(x)=exp(-a*x)*sin(w*x)

f = F(a=1.0, w=0.1)
from math import pi
print f.value(x=pi)

f.a = 2
print f.value(pi)

