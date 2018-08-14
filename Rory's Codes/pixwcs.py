"""pixwcs.py a program to take hubble pixel coordinates and convert them to WCS coordinates (RA and DEC)"""
#import modules
from astropy.wcs import WCS
from numpy import *
from astropy.io import fits
#load science header
header = fits.getheader('/Volumes/64FLASH/astro/photometry/NGC6819/raw/raw+/ib2o04/ib2o04020_drc.fits', 'sci')
#get the wcs information from the header
w = WCS(header)
#load the pixel coordinates of sources
xpos, ypos = loadtxt('/Volumes/64FLASH/dolphotresults/ib2o04/positions.txt', unpack=True)
#convert pixel coordinates to WCS coordinates
wx, wy = w.wcs_pix2world(xpos, ypos, 1)
#make these into an array
wcs=column_stack((wx,wy))
#save this to use in the next program
save("ib2o04wcs",wcs)
