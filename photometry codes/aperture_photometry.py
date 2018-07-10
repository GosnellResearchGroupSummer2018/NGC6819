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
from photutils import make_source_mask
from astropy.stats import sigma_clipped_stats

mask = make_source_mask(data, snr=2, npixels=5, dilate_size=10, sigclip_iters=None)
mean, median, std = sigma_clipped_stats(data, sigma=3.0, mask=mask, iters=None)
daofind = DAOStarFinder(fwhm=3.0, threshold=3*std)
sources = daofind(data)
positions = (sources['xcentroid'],sources['ycentroid'])

from photutils import CircularAperture
from photutils import CircularAnnulus
from photutils import aperture_photometry

apertures = CircularAperture(positions, r=3.)
annuli = CircularAnnulus(positions, r_in=6., r_out=8.)
apers = [apertures, annuli]
phot_table = aperture_photometry(data, apers)
bkg_mean = phot_table['aperture_sum_1'] / annuli.area()
bkg_sum = bkg_mean * apertures.area()
final_sum = phot_table['aperture_sum_0'] - bkg_sum
phot_table['residual_aperture_sum'] = final_sum
final_sum = np.asarray(final_sum)
np.set_printoptions(threshold=np.nan)
log = open("/Users/computationalphysics/Desktop/phot_table.txt", "w")
print(final_sum, file = log)
