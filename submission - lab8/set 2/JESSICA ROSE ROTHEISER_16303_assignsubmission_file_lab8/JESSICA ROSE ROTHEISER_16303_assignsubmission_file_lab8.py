import numpy as np
import matplotlib.pyplot as plt


def load(densityfile):
   data = {}
   data['temperature'], data['density'] = np.loadtxt(densityfile, unpack=True)
   return data


def fit(x, y, types):
   plt.plot(x, y, 'o')

   for deg, linecol in [(1, '#67001f'), (2, '#006837')]:
       coeff = np.polyfit(x, y, deg)
       y_fit = np.poly1d(coeff)
       plt.plot(x, y_fit(x), '--')

   x_range = x.max() - x.min()
   y_range = y.max() - y.min()
   plt.xlim([x.min() - 0.1 * x_range, x.max() + 0.1 * x_range])
   plt.ylim([y.min() - 0.1 * y_range, y.max() + 0.1 * y_range])
   plt.xlabel('Temperature')
   plt.ylabel('Density')
   plt.title('Temperature dependence of %s density' % types)
   plt.legend(['data',
               'fitted degree 1 polynomial',
               'fitted degree 2 polynomial'])
   plt.show()

#air density
data = load('density_air.dat')
fit(data['temperature'], data['density'], 'air')

# water density
data = load('density_water.dat')
fit(data['temperature'], data['density'], 'water')