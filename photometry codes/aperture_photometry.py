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

#Lines 16-18 bring in all the command necessary to detect sources in an image with high precision (using source masking)
from photutils import DAOStarFinder
from photutils import make_source_mask
from astropy.stats import sigma_clipped_stats

#Lines 21-22 create a mask that covers all the sources (signal:noise = 2:1) in an image and compute estimated background level and noise using the mask for higher accuracy. We are only interested in background noise levels in this case, which is defined as 'std'. This will be more accurate than the noise `make_source_mask` assumed for its signal:noise ratio, which it calculated on its own.
mask = make_source_mask(data, snr=2, npixels=5, dilate_size=10, sigclip_iters=None)
mean, median, std = sigma_clipped_stats(data, sigma=3.0, mask=mask, iters=None)

#Lines 24-26 find sources using a higher signal:noise ratio (3:1) and define their positions.
daofind = DAOStarFinder(fwhm=3.0, threshold=3*std)
sources = daofind(data)
positions = (sources['xcentroid'],sources['ycentroid'])

#Lines 29-31 bring in all commands necessary for aperture photometry
from photutils import CircularAperture
from photutils import CircularAnnulus
from photutils import aperture_photometry

#Lines 35-37 create aperture objects (a circle around each source with a concentric annulus around each circle) and group them in a 2x1 array called apers. Line 38 can be uncommented if you have an error estimate array and can be used to determine total error later.
apertures = CircularAperture(positions, r=3.)
annuli = CircularAnnulus(positions, r_in=6., r_out=8.)
apers = [apertures, annuli]
#error = #array based on WFC3 instrument that has error information for each pixel. Uncomment this line if you have such an array.

#Line 40 calculates the total number of counts in both the center circles and annuli around each source
phot_table = aperture_photometry(data, apers)#, error=error) #if you have an error array from line 31, uncomment the last argument of `aperture_photometry` to have another column in phot_table called 'aperture_sum_error'

#Lines 44-46 do the math necessary for aperture photometry. Using the annulus, and average background flux level is determined (counts in annulus divided by area of annulus), which is then multiplied by the area inside the center circle to find the total number of counts due to the background that are inside the circle. That value is subtracted from the measured flux inside the circle and you have an accurate estimate of the flux from the star itself. Line 48 adds a new column to phot_table with this information.
bkg_mean = phot_table['aperture_sum_1'] / annuli.area()
bkg_sum = bkg_mean * apertures.area()
final_sum = phot_table['aperture_sum_0'] - bkg_sum
phot_table['residual_aperture_sum'] = final_sum

#Lines 50-53 save an untruncated text file called 'phot_table.txt' that has columns "id, xcenter pix, ycenter pix, aperture_sum_0 (counts in the inner circle), aperture_sum_1 (counts in the annulus), and residual_aperture_sum (counts due to sources inside the circle)."
phot_table = np.array(phot_table)
np.set_printoptions(threshold=np.nan)
log = open("/Users/computationalphysics/Desktop/phot_table.txt", "w")
print(phot_table, file = log)

#Lines 56-63 can be uncommented to show an image with all the sources circled in blue. Line 62 can be further uncommented to plot the annuli as well. 
"""from astropy.visualization import LogStretch
from astropy.visualization.mpl_normalize import ImageNormalize

norm = ImageNormalize(stretch = LogStretch())
plt.imshow(data, cmap='Greys',origin='lower',norm=norm)
apertures.plot(color='blue', lw=1.5, alpha=.5)
#annuli.plot(color='blue', lw=1.5, alpha=.5) #uncomment this line to plot the annuli
plt.show()"""
