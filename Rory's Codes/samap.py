"""samap.py an aperture photometry program using sample images"""
from pylab import *
from scipy import *
from numpy import *
from photutils import datasets
from photutils import CircularAperture
from photutils import aperture_photometry
from astropy.io import ascii
#import the data needed from source detection output
xcentroid, ycentroid = loadtxt('samsdout.txt', usecols=(1,2), skiprows=1, unpack=True)
#make arrays of x and y positions
xpos= array(xcentroid)
ypos= array(ycentroid)
#turn those two arrays into a N*2 array
pos=column_stack((xpos,ypos))
#make an aperture for each source. r is the radius of the aperture
apertures = CircularAperture(pos, r=3.)
#define where to look for the counts inside each aperture
data = load("data.npy")
#perform aperture photometry on the data in the given apertures
phot_table = aperture_photometry(data, apertures)
print(phot_table)
#save the resulting table to an output text file
ascii.write(phot_table, 'samapout.txt',overwrite=True)
