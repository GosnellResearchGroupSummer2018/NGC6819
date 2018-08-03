"""seppractice.py"""

import numpy as np
import sep
from pylab import *

# additional setup for reading the test image and displaying plots
import fitsio
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['figure.figsize'] = [10., 8.]

# read image into standard 2-d numpy array
data = fitsio.read("/Volumes/64FLASH/astro/photometry/NGC6819/raw/raw+/ibop04/ibop04giq_flc.fits")

# show the image
m, s = np.mean(data), np.std(data)
plt.imshow(data, interpolation='nearest', cmap='gray', vmin=m-s, vmax=m+s, origin='lower')
plt.colorbar();

show()
