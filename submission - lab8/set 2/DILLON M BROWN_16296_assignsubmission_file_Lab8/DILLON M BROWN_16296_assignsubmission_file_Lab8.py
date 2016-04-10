import numpy as np
import matplotlib.pyplot as plt
def data_parse(file):
    x = []
    y = []
    with open(file) as dw:
        for line in dw:
            if line[0] != '#':
                line = line.strip()
                if len(line)<1:
                    continue
                else:
                    line = line.split('   ')
                    x.append(float(line[0]))
                    y.append(float(line[1]))
        return x,y
def data_plot(x,y,title):
    coeff1 = np.polyfit(x,y,1)
    coeff2 = np.polyfit(x,y,2)
    p1 = np.poly1d(coeff1)
    p2 = np.poly1d(coeff2)
    plt.plot(x,y,'bo',label = 'Raw Data')
    plt.plot(x,p1(x),'r--',label = '1 degree Fit')
    plt.plot(x,p2(x),'g--',label = '2 degree Fit')
    plt.legend()
    plt.title(title)
    plt.xlabel('Temperature')
    plt.ylabel('Density')
    plt.show()
    return

wtr = data_parse('density_water.dat')
air = data_parse('density_air.dat')

wtr_temp = np.array(wtr[0])
wtr_dens = np.array(wtr[1])
air_temp = np.array(air[0])
air_dens = np.array(air[1])

data_plot(wtr_temp,wtr_dens,'Water Density as a function of Temp')
data_plot(air_temp,air_dens,'Air Density as a function of Temp')