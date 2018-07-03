#This code is intended to take in a .fits file and produce a reverse black and white image that uses blue circles to show 5σ detections. This image can be used to do psf or aperture photometry that will give data in counts about the star's flux.

import numpy as np
from matplotlib import pylab
from IPython.core.pylabtools import *
from pylab import *
from numpy import *
from astropy.visualization import LogStretch
from astropy.visualization.mpl_normalize import ImageNormalize
from astropy.io import fits

hdu = fits.open("/Users/computationalphysics/Desktop/ib2o01020_drz.fits")[1]
data = hdu.data[0:, 0:]

norm = ImageNormalize(stretch = LogStretch())
from astropy.stats import sigma_clipped_stats
from photutils import DAOStarFinder

mean, median, std = sigma_clipped_stats(data, sigma=3.0,iters=5)

daofind = DAOStarFinder(fwhm=3.0, threshold=5*std)
sources = daofind(data - median)
log = open("/Users/computationalphysics/Desktop/sources.txt", "w")
print(sources, file = log)

from photutils import CircularAperture

x = (sources['xcentroid'])
y = (sources['ycentroid'])
positions = (x,y)

plt.imshow(data, cmap='gray_r',origin='lower',norm=norm)
apertures = CircularAperture(positions, r=3.)
apertures.plot(color='blue', lw=1.5, alpha=0.5)
plt.show()
