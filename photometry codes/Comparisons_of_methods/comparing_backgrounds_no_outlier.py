import matplotlib.pyplot as plt
import numpy as np
from IPython.core.pylabtools import *
from pylab import *
from numpy import *

from astropy.io import fits

hdu = fits.open("/Users/computationalphysics/Desktop/ib2o01020_drz.fits")[1]
data = hdu.data[3000:3200, 3000:3200]

from photutils import DAOStarFinder
from photutils import make_source_mask
from astropy.stats import sigma_clipped_stats

mask = make_source_mask(data, snr=2, npixels=5, dilate_size=10, sigclip_iters=None)
mean, median, std = sigma_clipped_stats(data, sigma=3.0, mask=mask, iters=None)
daofind_nbkg = DAOStarFinder(fwhm=3.0, threshold=3*std)
daofind_ybkg = DAOStarFinder(fwhm=3.0, threshold=3*std)
sources_nbkg = daofind_nbkg(data - median)
sources_ybkg = daofind_ybkg(data)
positions_nbkg = (sources_nbkg['xcentroid'],sources_nbkg['ycentroid'])
positions_ybkg = (sources_ybkg['xcentroid'],sources_ybkg['ycentroid'])

from photutils import CircularAperture
from photutils import CircularAnnulus
from photutils import aperture_photometry

apertures_nbkg = CircularAperture(positions_nbkg, r=3.)
annuli_nbkg = CircularAnnulus(positions_nbkg, r_in=6., r_out=8.)
apers_nbkg = [apertures_nbkg, annuli_nbkg]
err_nbkg =
phot_table_nbkg = aperture_photometry(data, apers_nbkg, error=err_nbkg)
bkg_mean_nbkg = phot_table_nbkg['aperture_sum_1'] / annuli_nbkg.area()
bkg_sum_nbkg = bkg_mean_nbkg * apertures_nbkg.area()
final_sum_nbkg = phot_table_nbkg['aperture_sum_0'] - bkg_sum_nbkg

apertures_ybkg = CircularAperture(positions_ybkg, r=3.)
annuli_ybkg = CircularAnnulus(positions_ybkg, r_in=6., r_out=8.)
apers_ybkg = [apertures_ybkg, annuli_ybkg]
err_ybkg =
phot_table_ybkg = aperture_photometry(data, apers_ybkg, error=err_ybkg)
bkg_mean_ybkg = phot_table_ybkg['aperture_sum_1'] / annuli_ybkg.area()
bkg_sum_ybkg = bkg_mean_ybkg * apertures_ybkg.area()
final_sum_ybkg = phot_table_ybkg['aperture_sum_0'] - bkg_sum_ybkg

x = np.linspace(-1,12,50)
y = np.linspace(-1,12,50)

plt.plot(final_sum_nbkg, final_sum_ybkg, 'ro')
plt.plot(x,y, 'b-')
plt.xlim([-.5, 1.5])
plt.ylim([-.5, 1.5])
plt.xlabel('Flux rates w/ background level subtracted before source detection (counts/s)')
plt.ylabel('Flux rates w/o background level subtracted before source detection (counts/s)')
plt.title('Comparing flux rates calculated w/ different source detection methods')
plt.errorbar(final_sum_nbkg, final_sum_ybkg, xerr=phot_table_nbkg['aperture_sum_err'], yerr=phot_table_ybkg['aperture_sum_err'])
plt.show()
