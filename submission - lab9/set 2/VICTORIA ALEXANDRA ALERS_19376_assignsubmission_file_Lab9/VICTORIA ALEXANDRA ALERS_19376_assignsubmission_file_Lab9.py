#1________________________________
from math import sin, exp


class F:

    def __init__(self, a, w):
        self.a = a
        self.w = w

    def value(self, x):
        a = self.a
        w = self.w
        return exp(-a * w) * sin(w * x)

from math import pi
f = F(a=1.0, w=0.1)
print (f.value(x=pi))
f.a = 2
print (f.value(pi))

#2---------------------------------------------
class Simple:
    def __init__(self, i):
        #super().__init__()
        self.i=i
    def double(self):
        self.i = self.i + self.i


        
s1=Simple(4)
for i in range(4):
    s1.double()
print(s1.i)

s2=Simple('Hello')
s2.double(); s2.double()
print(s2.i)
s2.i=100
print(s2.i)
