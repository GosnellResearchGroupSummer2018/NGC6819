"""plotpos.py a program to plot dolphot output on the reference image
used for photometry"""
#import modules
from pylab import *
from scipy import *
from numpy import *
from photutils import CircularAperture
from astropy.io import fits

#import data
pos = loadtxt('/Volumes/64FLASH/dolphotresults/ib2o01/positions.txt')
clf()
hdu = fits.open("/Volumes/64FLASH/astro/photometry/NGC6819/raw/raw+/ib2o01/ib2o01020_drc.fits")[1]
data = hdu.data

#plot the data
apertures = CircularAperture(pos, r=8)
#show everything- v min and v max define the end points of the color mapping
imshow(data, cmap='coolwarm', origin='lower', vmin=0, vmax=5)
apertures.plot(color='xkcd:electric purple', lw=2, alpha=0.5)
savefig('ib2o01.png')
show()
