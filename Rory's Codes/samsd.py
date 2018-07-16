"""samsd.py a source detection program using sample images"""
#import modules
from astropy.stats import sigma_clipped_stats
from pylab import *
from scipy import *
from numpy import *
from photutils import datasets
from photutils import DAOStarFinder
from astropy.stats import mad_std
from astropy.io import ascii
#import data from background detection
data = load("data.npy")
bkrd,std = loadtxt('sambdout.txt',usecols= (1,2),unpack=True)
#DAOStarFinder is a routine in photutils
#fwhm sets the
daofind = DAOStarFinder(fwhm=2, threshold=5*std)
# perform DAOStarFinder on the data with the median background subtracted
sources = daofind(data-bkrd)
#print the results of our daofind
print(sources)
#NEW way to save data, fewer steps, works with mixins, use ascii.write
ascii.write(sources, 'samsdout.txt', overwrite=True)
#extract the position data as arrays
xpos= array(sources['xcentroid'])
ypos= array(sources['ycentroid'])
#turn those two arrays into a N*2 array
pos=column_stack((xpos,ypos))
#save this to use in the next program
save("pos",pos)
#plot the positions of these sources on the image
from photutils import CircularAperture
#number the data points
#define a variable for the for the loop
close()
N = len(xpos)
fig, ax = plt.subplots()
#run for loop
#i+1 is neccesary because the data is ouput from 1-N+1 but i goes from 0-N
for i in range (0,N):
    ax.annotate("%d" % (i+1), (xpos[i],ypos[i]))
#plot the apertures
apertures = CircularAperture(pos, r=8)
#show everything- v min and v max define the end points of the color mapping
imshow(data-bkrd, cmap='coolwarm', origin='lower', vmin=0, vmax=1)
apertures.plot(color='xkcd:electric purple', lw=2, alpha=0.5)
#save the figure
savefig('sourcefigf2t5v1.png')
show()
