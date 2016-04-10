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
                
    plt.show()

data = poly1d('density_air.dat')
polyfit(data['temperature'], data['density'], 'air')

data = poly1d('density_water.dat')
polyfit(data['temperature'], data['density'], 'water')

print ("Best fit for air: y = -0.006x + 1.34")
print ("Best fit for water: -0.005 * x**2 - 0.06 + 1000")