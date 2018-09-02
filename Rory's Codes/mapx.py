"""mapx.py a program to plot the x ray sources with their identifiers"""
from pylab import *
from scipy import *
from numpy import *
from photutils import CircularAperture
from astropy.io import fits
from astropy.wcs import WCS
ax = plt.subplot()
xra,xdec=loadtxt("xa.txt",unpack=True)
ax.scatter(xra,xdec, s=60,edgecolor='purple', facecolor='none')
N=len(xra)
for i in range (0,N):
    ax.annotate("X%d" % (i+1), (xra[i],xdec[i]))
ax.invert_xaxis()
show()
