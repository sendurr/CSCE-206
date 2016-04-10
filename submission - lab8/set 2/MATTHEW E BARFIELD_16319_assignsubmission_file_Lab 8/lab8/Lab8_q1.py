''' write code to read the density vs temperature of water and air data into two lists/
arrays. generate a polynomial function that fit the data. plot the results of the raw data
and the fit polynomial function'''


import numpy as np
import matplotlib.pyplot as plt
import sys

#step one. Read the density vs temperature
def density(densityfile):
    infile = open(densityfile, 'r')
    data = {'Temperature': [], 'Density': []}

    for line in infile:
        if line.lstrip()[0] == '#':   # skips blank line or comment
            continue
        else:
            values = line.split()
            data['Temperature'].append(float(values[0]))
            data['Density'].append(float(values[1]))
    data['Temperature'] = np.array(data['Temperature'])
    data['Density'] = np.array(data['Density'])
    infile.close()
    return data



def plot(x, y, substance):
    plt.plot(x, y, 'o'
    
    plt.xlabel('Temperature')
    plt.ylabel('Density')
    plt.title('Temperature Dependence of %s Density' % substance)
    # set axis ranges appropriately
    x_range = x.max() - x.min()
    y_range = y.max() - y.min()
    plt.xlim([x.min() - 0.1 * x_range, x.max() + 0.1 * x_range])
    plt.ylim([y.min() - 0.1 * y_range, y.max() + 0.1 * y_range])
    plt.show()


try:
    densityfile = sys.argv[1]
    substance = sys.argv[2]
except IndexError:
    print 'The density file name and substance must be given \
        on the command line'
    sys.exit(1)

data = load(density_air.dat), load(density_water.dat)
plot(data['Temperature'], data['Density'], substance)
