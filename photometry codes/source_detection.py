#This code is intended to take in a .fits file and produce a reverse black and white 2D array (presented as pixels in an image) showing all the electromagnetically radiative objects (sources) in a section of the sky. It uses blue circles to show the location of the sources.

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

#Lines 18-20 bring in the commands necessary to determine the background flux of the image and find sources therein.
from photutils import make_source_mask
from astropy.stats import sigma_clipped_stats
from photutils import DAOStarFinder

#Lines 20-20 create a mask that hides all sources in the image, calculate the background flux level  and noise of the image after those points are removed, define them as "median" and "std" respectively, define the command "daofind" as something that will ignore the mask and find sources with flux greater than 5 times the calculated background noise coming from a circle around the source that is three times the "full-width half-maximum" of that source (a function of sigma, the fwhm assumes the measured flux dies off as a gaussian and is a measure of that gaussian's width), find those sources after subtracting the background flux level from the total, define the result "sources" and save them to a text document on the desktop.
mask = make_source_mask(data, snr=2, npixels=5, dilate_size=10, sigclip_iters=None)
mean, median, std = sigma_clipped_stats(data, sigma=3.0, mask=mask, iters=None)
daofind = DAOStarFinder(fwhm=3.0, threshold=3*std)
sources = daofind(data - median)
sources = array(sources)
np.set_printoptions(threshold=np.nan)
log = open("/Users/computationalphysics/Desktop/sources.txt", "w")
print(sources, file = log)

#Lines 33-35 bring in the commands necessary to perform aperture photometry (though we're only drawing circles) using photutils and to plot the aperture objects with precision.
from photutils import CircularAperture
from astropy.visualization import LogStretch
from astropy.visualization.mpl_normalize import ImageNormalize

#Lines 38-39 define "positions" as the "center of flux" (a term I made up analogous to center of mass) of each source and "norm" as a normalization function that helps determine the size of a pixel in the output image.
positions = (sources['xcentroid'],sources['ycentroid'])
norm = ImageNormalize(stretch = LogStretch())

#Lines 41-45 create an image that contains all the flux data we've been working with (from line 14), draw blue circles of radius three arcseconds, places the circles on the spots defined by "positions" (so hopefully directly over each source), and shows off the result.
plt.imshow(data, cmap='Greys',origin='lower',norm=norm)
apertures = CircularAperture(positions, r=3.)
apertures.plot(color='blue', lw=1.5, alpha=.5)
plt.show()
