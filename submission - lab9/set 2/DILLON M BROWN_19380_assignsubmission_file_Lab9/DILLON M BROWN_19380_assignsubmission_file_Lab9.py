from math import *

##Q1

class F:
    def __init__(self,a,w):
        self.a = a
        self.w = w
    def value(self,x):
        a,w = self.a,self.w
        return exp(-1*a*x)*sin(w*x)

f = F(a=1.0,w=0.1)
print f.value(x=pi)
f.a = 2
print f.value(pi)

##Q2

class Simple:
    def __init__(self,i):
        self.i = i
    def double(self):
        self.i += self.i

s1 = Simple(4)
print s1.i
for i in range(4):
    s1.double()
print s1.i

s2 = Simple('Hello')
s2.double(); s2.double()
print s2.i
s2.i = 100
print s2.i

