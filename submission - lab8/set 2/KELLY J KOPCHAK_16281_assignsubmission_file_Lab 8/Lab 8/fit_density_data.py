import numpy as np
import matplotlib.pyplot as plt

def poly1d(coeff):
    data = {}
    data['temperature'], data['density'] = np.loadtxt(coeff, unpack=True)
    return data


def polyfit(x, y, deg):
    plt.plot(x, y, 'o')
    
    for deg, linecol in [(1, '#67001f'), (2, '#006837')]:
        coeff = np.polyfit(x, y, deg)
        y_fit = np.poly1d(coeff)
        plt.plot(x, y_fit(x), '--')

    
    x_range = x.max() - x.min()
    y_range = y.max() - y.min()
    plt.xlim([x.min() - 0.1 * x_range, x.max() + 0.1 * x_range])
    plt.ylim([y.min() - 0.1 * y_range, y.max() + 0.1 * y_range])
    plt.xlabel('Temp')
    plt.ylabel('Density')
   
    plt.show()

data = poly1d('density_air.dat')
polyfit(data['temperature'], data['density'], 'air')

data = poly1d('density_water.dat')
polyfit(data['temperature'], data['density'], 'water')

print "Best fit for air: y = -0.006*x + 1.36"
print "Best fit for water: y = -0.005*x**2 - 0.066*x + 1010"
