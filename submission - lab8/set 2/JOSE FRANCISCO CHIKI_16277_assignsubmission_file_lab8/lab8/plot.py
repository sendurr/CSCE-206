from numpy import *
import matplotlib.pyplot as plt

dataa = loadtxt('density_air.dat', dtype=float)  # read table of floats
ta = dataa[:,0]  # column with index 0
da = dataa[:,1]  # column with index 1
print ta
print da

dataw = loadtxt('density_water.dat', dtype=float)  # read table of floats
tw = dataw[:,0]  # column with index 0
dw = dataw[:,1]  # column with index 1
print tw
print dw

plt.figure(1)
coeffa=polyfit(ta,da,1)
pa=poly1d(coeffa)
print pa
da_fitted=pa(ta)
plt.plot(ta,da,'r-',ta,da_fitted,'b-')
plt.show(plt.plot(ta,da,'r-',ta,da_fitted,'b-'))

plt.figure(2)
coeffw=polyfit(tw,dw,2)
pw=poly1d(coeffw)
print pw
dw_fitted=pw(tw)
plt.plot(tw,dw,'r-',tw,dw_fitted,'b-')
plt.show(plt.plot(tw,dw,'r-',tw,dw_fitted,'b-'))

plt.show()

