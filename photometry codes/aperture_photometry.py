#Lines 4-8 bring in the most basic databases that this code needs to understand all the commands below it.
import numpy as np
from matplotlib import pylab
from IPython.core.pylabtools import *
from pylab import *
from numpy import *

#Line 11 brings in the command necessary to call data.
from astropy.io import fits

#Lines 14-15 tell the program where to find data (which, for this program to work, should be on the desktop) and defines that data as "data".
hdu = fits.open("/Users/computationalphysics/Desktop/ib2o01020_drz.fits")[1]
data = hdu.data[3000:3200, 3000:3200] #This image is 5644x5895 piels, and I want to restrict my search to the very small section in the center because the edges of these images are noisy and this code is optimized to work on smaller images.

from photutils import DAOStarFinder
from astropy.visualization import LogStretch
from astropy.visualization.mpl_normalize import ImageNormalize

from photutils import CircularAperture
apertures = CircularAperture(positions, r=3.)


daofind = DAOStarFinder(fwhm=3.0, threshold=3*std)
sources = daofind()
print(sources)
