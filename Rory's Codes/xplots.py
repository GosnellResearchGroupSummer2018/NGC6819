"""xplots.py
a program to plot the position of the sources and all of the x ray sources on a mosaic of the whole cluster"""
#import modules
from pylab import *
from scipy import *
from numpy import *
from photutils import CircularAperture
from astropy.io import fits
from astropy.wcs import WCS
from astropy import units as u
from astropy.visualization.wcsaxes import SphericalCircle
#do awk stuff here with numpy
#dolph = loadtxt('/Volumes/64FLASH/dolphotresults/ib2o01/ngc6819_wfc3_grid4.phot')
#gdolph=dolph[where(all(dolph[:,6] >= -.3 * dolph[:,6] <= .3 * dolph[:,23]  == 0 * dolph[:,5]  >= 75 * dolph[:,7] <= 1 * dolph[:,9] <= 1))]
#import data
ra, dec =loadtxt("6819xmatchedcat.txt", usecols=(0,1), unpack=True)
xra,xdec=loadtxt("xa.txt",unpack=True)
clf()
hdu = fits.open("/Volumes/64FLASH/mosaic.fits")[0]
data = hdu.data
wcs = WCS(hdu.header)
#subplot(projection=wcs)
#grid(color='white', ls='solid')
#plot the data
N=len(ra)
print(N)
xn=len(xra)
xer=loadtxt("xerrors.txt")
ax = plt.subplot(projection=wcs)
#show everything- v min and v max define the end points of the color mapping
xsources=[]
sources=[]
for i in range(0,xn):
    r = SphericalCircle((xra[i] * u.deg, xdec[i] * u.deg), xer[i] * u.arcsec,
        edgecolor='purple', facecolor='none',
        transform=ax.get_transform('fk5'))
    xsources.append(r)
    text(xra[i], xdec[i], str(i+1), color="red",transform=ax.get_transform('fk5'), fontsize=12)
#for i in range(0,N):
#    r = SphericalCircle((ra[i] * u.deg, dec[i] * u.deg), .5 * u.arcsec,
#        edgecolor='orange', facecolor='none',
#        transform=ax.get_transform('fk5'))
#    sources.append(r)
imshow(data, cmap='Greys', origin='lower', vmin=0, vmax=1)
ax.scatter(ra,dec, transform=ax.get_transform('fk5'), s=100,
    edgecolor='orange', facecolor='none')
for i in range(0,xn):
    ax.add_patch(xsources[i])
#for i in range(0,N):
#    ax.add_patch(sources[i])
#ax.scatter(xra,xdec, transform=ax.get_transform('fk5'), s=60,
#           edgecolor='purple', facecolor='red')
#N=len(xra)
#for i in range (0,N):
#    ax.annotate("X%d" % (i+1), (xra[i],xdec[i]),xycoords='data')
#imshow(data, cmap='rainbow', origin='lower', vmin=0, vmax=1)
show()
