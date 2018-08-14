"""plotpos.py a program to plot dolphot output on the reference image
used for photometry"""
#import modules
from pylab import *
from scipy import *
from numpy import *
from photutils import CircularAperture
from astropy.io import fits
#do awk stuff here with numpy
#dolph = loadtxt('/Volumes/64FLASH/dolphotresults/ib2o02/ngc6819_wfc3_grid4.phot')
#gdolph=dolph[where(all(dolph[:,6] >= -.3 * dolph[:,6] <= .3 * dolph[:,23]  == 0 * dolph[:,5]  >= 75 * dolph[:,7] <= 1 * dolph[:,9] <= 1))]

#import data
pos = loadtxt('/Volumes/64FLASH/dolphotresults/ib2o02/positions.txt')
#pos = gdolph[:,2,:,3]
#print(pos)
#print(len(pos))
clf()
hdu = fits.open("/Volumes/64FLASH/astro/photometry/NGC6819/raw/raw+/ib2o02/ib2o02020_drc.fits")[1]
data = hdu.data

#plot the data
apertures = CircularAperture(pos, r=8)
#show everything- v min and v max define the end points of the color mapping
imshow(data, cmap='coolwarm', origin='lower', vmin=0, vmax=5)
apertures.plot(color='xkcd:electric purple', lw=2, alpha=0.5)
savefig('ib2o02.png')
show()
