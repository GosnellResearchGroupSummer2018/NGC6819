"""samap.py an aperture photometry program using sample images"""
from pylab import *
from scipy import *
from numpy import *
from photutils import datasets
from photutils import CircularAperture
from photutils import aperture_photometry
from astropy.io import ascii
#import the data needed from source detection output
pos=load("pos.npy")
#make an aperture for each source. r is the radius of the aperture
apertures = CircularAperture(pos, r=8)
#tell the program where map with counts is
data = load("data.npy")
#perform aperture photometry on the data in the given apertures
phot_table = aperture_photometry(data, apertures)
#save the resulting table to an output text file
ascii.write(phot_table, 'samapout.txt',overwrite=True)
