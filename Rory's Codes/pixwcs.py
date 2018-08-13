"""pixwcs.py a program to take hubble pixel coordinates and convert them to WCS coordinates (RA and DEC)"""

from astropy.wcs import WCS
from numpy import *
from astropy.io import fits
header = fits.getheader('/Volumes/64FLASH/astro/photometry/NGC6819/raw/raw+/ibop04/ibop04020_drc.fits', 'sci')
w = WCS(header)
xpos, ypos = loadtxt('/Volumes/64FLASH/dolphotresults/ibop04/positions.txt', unpack=True)
wx, wy = w.wcs_pix2world(xpos, ypos, 1)
