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
from astropy.io import ascii
#import data from background detection
#image = datasets.load_star_image()
data = load("data.npy")
bkrd,std = loadtxt('sambdout.txt',usecols= (1,2),unpack=True)
#DAOStarFinder is a routine in photutils
#fwhm sets the
daofind = DAOStarFinder(fwhm=10., threshold=3.*std)
# perform DAOStarFinder on the data with the median background subtracted
sources = daofind(data-bkrd)
#print the results of our daofind
#print(sources)
#NEW way to save data, fewer steps, works with mixins, use ascii.write
ascii.write(sources, 'samsdout.txt', overwrite=True)
#plot the positions of these sources on the image
from astropy.visualization import SqrtStretch
from astropy.visualization.mpl_normalize import ImageNormalize
from photutils import CircularAperture
positions = (sources['xcentroid'], sources['ycentroid'])
apertures = CircularAperture(positions, r=4)
norm = ImageNormalize(stretch=SqrtStretch())
imshow(data-bkrd, cmap='Greys', origin='lower', norm=norm)
apertures.plot(color='blue', lw=1.5, alpha=0.5)
#save the firgure rather than displaying it
savefig('sourcefig.png')
