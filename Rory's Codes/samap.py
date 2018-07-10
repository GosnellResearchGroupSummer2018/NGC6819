"""samap.py an aperture photometry program using sample images"""
from pylab import *
from scipy import *
from numpy import *
from photutils import datasets
from photutils import CircularAperture
from photutils import aperture_photometry
from astropy.io import ascii
id, xcentroid, ycentroid, sharpness, roundness1, roundness2, npix, sky, peak, flux, mag = loadtxt('samsdout.txt',skiprows=1, unpack=True)
xpos= array(xcentroid)
ypos= array(ycentroid)
pos=column_stack((xpos,ypos))
apertures = CircularAperture(pos, r=3.)
data = datasets.make_100gaussians_image()
phot_table = aperture_photometry(data, apertures)
print(phot_table)
ascii.write(phot_table, 'samapout.txt',overwrite=True)
