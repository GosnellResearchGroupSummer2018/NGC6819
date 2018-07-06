"""samsd.py a source detection program using sample images"""
#import modules
from astropy.stats import sigma_clipped_stats
from pylab import *
from scipy import *
from numpy import *
from photutils import datasets
from photutils import DAOStarFinder
from astropy.stats import mad_std
from pandas import *
#import data from background detection
image = datasets.make_100gaussians_image()
bkrd,std = loadtxt('sambdout.txt',usecols= (1,2),unpack=True)
#DAOStarFinder is a routine in photutils
#fwhm sets the
daofind = DAOStarFinder(fwhm=10., threshold=3.*std)
# perform DAOStarFinder on the data with the median background subtracted
sources = daofind(image-bkrd)
#print the results of our daofind
print(sources)
#to get the table into a savable format, I converted it into a pandas format
samsdout = sources.to_pandas()
#then i converted it into a numpy array that i saved with savetxt
samsdouta=array(samsdout)
savetxt('samsdout.txt',samsdouta,fmt='%f')
