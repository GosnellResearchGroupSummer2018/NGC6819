"""samsd.py a source detection program using sample images"""
#import modules
from astropy.stats import sigma_clipped_stats
from pylab import *
from scipy import *
from numpy import *
from photutils import datasets
from photutils import DAOStarFinder
from astropy.stats import mad_std
#import data from background detection
image = datasets.make_100gaussians_image()
bkrd = loadtxt('sambdout.txt',usecols= 1,unpack=True)
daofind = DAOStarFinder(fwhm=4., threshold=3.*bkrd)
sources = daofind(image)
print(sources)
log = open('samsdout.txt', "w")
print(sources, file = log)
close()
#sourcea = array(sources)
#sourcear = transpose(sourcea)
#savetxt('samsdout.txt', [sourcear],fmt='%f')
