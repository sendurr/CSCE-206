v0=1
g=9.81
n=11
tf=(2*v0)/g
stepsize=(tf/n)

t=0
while t<tf:
    yt=v0*t-.5*g*t**2
    print ("%.4f" % t), ("%.4f" % yt)
    t+=stepsize