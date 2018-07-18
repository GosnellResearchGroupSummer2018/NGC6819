#Lines 4-7 bring in the most basic databases that this code needs to understand all the commands below it.
import numpy as np
from matplotlib import pylab
from IPython.core.pylabtools import *
from pylab import *
from numpy import *

#Line 9 brings in the command necessary to call data.
from astropy.io import fits

#Lines 12-13 tell the program where to find data (which, for this program to work, should be on the desktop) and define that data as "data."
hdu = fits.open("/Users/computationalphysics/Desktop/ib2o03p8q_flc.fits")[1]
data = hdu.data[500:800,1700:2000] #This image is 5644x5895 pixels, and I want to restrict my search to the very small section in the center because the edges of these images are noisy and this code is optimized to work on smaller images.

#Lines 16-18 bring in all the command necessary to detect sources in an image with high precision (using source masking)
from photutils import DAOStarFinder
from photutils import make_source_mask
from astropy.stats import sigma_clipped_stats

#Lines 21-22 create a mask that covers all the sources (something is a source if its signal:noise = 2:1) in an image and compute estimated background level and noise using the mask for higher accuracy. We are only interested in background noise in this case, not level, which is defined as 'std'. This will be more accurate than the noise `make_source_mask` assumed for its signal:noise ratio, which it calculated on its own.
mask = make_source_mask(data, snr=2, npixels=5, dilate_size=10, sigclip_iters=None)
mean, median, std = sigma_clipped_stats(data, sigma=3.0, mask=mask, iters=None)

#Lines 25-27 find sources in the image using a higher signal:noise ratio (3:1) and more precise noise estimate. They then define the sources' positions.
daofind = DAOStarFinder(fwhm=4.3, threshold=7*std)
sources = daofind(data)
positions = (sources['xcentroid'],sources['ycentroid'])

#Lines 30-32 bring in all commands necessary for aperture photometry
from photutils import CircularAperture
from photutils import CircularAnnulus
from photutils import aperture_photometry

#Lines 35-37 create aperture objects (a circle around each source with a concentric annulus around each circle) and group them in a 2x1 array called apers.
apertures = CircularAperture(positions, r=3.)
annuli = CircularAnnulus(positions, r_in=6., r_out=8.)
apers = [apertures, annuli]

#Lines 40-41 replace all negatives in 'data' with 0, estimate the uncertainty in the number of counts at each pixel from Possion, and define that uncertainty as 'error'
data[data < 0] = 0
error = np.sqrt(data)

#Line 44 calculates the total number of counts in both the center circles and annuli around each source and propogates the uncertainty in each pixel over the entire aperture object.
phot_table = aperture_photometry(data, apers, error=error)

#Lines 47-50 do the math necessary for aperture photometry. Assuming the annulus only contains counts due to the background, an average background flux level is determined by calculating total counts in the annulus divided by the area of annulus. This average is then multiplied by the area inside the center circle to find counts due to the background that are inside the circle. That value is subtracted from the measured flux rate inside the circle and you have an accurate estimate of the flux rate of the star itself. Line 48 adds a new column to phot_table with this information.
bkg_mean = phot_table['aperture_sum_1'] / annuli.area()
bkg_sum = bkg_mean * apertures.area()
final_sum = phot_table['aperture_sum_0'] - bkg_sum
phot_table['residual_aperture_sum'] = final_sum

#Lines 53-56 calculate the total error in the same way as the flux in counts is calculated above
err_mean = phot_table['aperture_sum_err_1'] / annuli.area()
err_sum = err_mean * apertures.area()
final_err = phot_table['aperture_sum_err_0'] - err_sum
phot_table['residual_err_sum'] = final_err

from astropy.io import ascii
#Lines 59-62 save an untruncated text file called 'phot_table.txt' that has columns "id, xcenter pix, ycenter pix, aperture_sum_0 (counts in the inner circle), aperture_sum_1 (counts in the annulus), aperture_sum_err_0 (total uncertainty from annulus), aperture_sum_err_1 (total uncertainty in center circle), residual_aperture_sum (counts due to sources inside the circle), and residual_sum_err (total uncertainty in source flux rate)"
"""ascii.write(phot_table, 'phot_table.txt', overwrite=True)"""
phot_table = np.array(phot_table)
np.set_printoptions(threshold=np.nan)
log = open("/Users/computationalphysics/Desktop/phot_table.txt", "w")
print(phot_table, file = log)

#Lines 65-66 bring in the tools necessary to draw an undistorted image
from astropy.visualization import LogStretch
from astropy.visualization.mpl_normalize import ImageNormalize

plt.subplot(211)
plt.title('RA = {-19:41:15.0244 U -19:41:155.6276}, Dec = {40:12:39.279 U 40:12:23.988}')
norm = ImageNormalize(stretch = LogStretch())
plt.imshow(data, cmap='cool',origin='lower',norm=norm, vmax=12000)

#Lines 69-73 show all the sources in an image by circling them in blue. Line 74 can be uncommented to show the annuli as well
plt.subplot(212)
plt.title('Sources in RA = {-19:41:15.34 U -19:41:13.74}, Dec = {40:12:26.23 U 40:12:29.34}')
norm = ImageNormalize(stretch = LogStretch())
plt.imshow(data, cmap='cool',origin='lower',norm=norm, vmax=12000)
apertures.plot(color='blue', lw=1.5, alpha=.5)
N = len(sources['xcentroid'])
xpos = sources['xcentroid']
ypos = sources['ycentroid']
for i in range (0,N):
    plt.annotate("%d" % (i+1), (xpos[i],ypos[i]))
#annuli.plot(color='blue', lw=1.5, alpha=.5) #uncomment this line to plot the annuli

#Lines 77-82 create a plot that shows the flux rates and implied uncertainties for each source. Sources are numbered 1-147
"""plt.subplot(212)
plt.errorbar(phot_table['id'], phot_table['residual_aperture_sum'], yerr=phot_table['residual_err_sum'], fmt='o', markersize=2.5, ecolor='r', barsabove=True)
plt.xlabel('Source ID')
plt.ylabel('Fluxes (counts)')
plt.title('Fluxes of Above Sources')"""
plt.show()
