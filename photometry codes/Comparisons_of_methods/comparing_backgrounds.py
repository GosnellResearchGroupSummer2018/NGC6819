import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

nbkg = open("/Users/computationalphysics/Desktop/phot_table_nbkg.txt", "r")
ybkg = open("/Users/computationalphysics/Desktop/phot_table_ybkg.txt", "r")
nbkg = list(nbkg)
ybkg = list(ybkg)

x = np.linspace(0, 37, 100)
y = np.linspace(0, 37, 100)
plt.xlabel('Fluxes calculated by subtracting the median background level before aperture photometry')
plt.ylabel('Fluxes calculated without subtracting the median background level before aperture photometry')
plt.title('Comparing fluxes calculated using different backgrounds')
plt.plot(x,y)
plt.plot(nbkg, ybkg, 'ro')
plt.show()
