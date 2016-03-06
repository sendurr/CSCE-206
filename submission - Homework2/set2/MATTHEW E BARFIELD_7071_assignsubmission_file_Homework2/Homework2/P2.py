
(v,g,t)=(5.0,9.81,0.0)

x=2.0*(v/g)
i=0
step=x/11

print "t\t\t\ty(t)"
while t<x:    
    y=(v*t)-(0.5*g*t**2)
    print "%f\t%f"%(t,y)
    t+=step    
