"""catmat.py a program to match sources between different source catalogs"""
#import modules
from astropy.coordinates import SkyCoord
from astropy import units as u
from numpy import *
#import position wcs data
ib2o02wcs = load("ib2o02wcs.npy")
#define first column as ra
ra1 = ib2o02wcs[:,0]
#second column as dec
dec1 = ib2o02wcs[:,1]
#do it with the other data
ib2o01wcs = load("ib2o01wcs.npy")
ra2 = ib2o01wcs[:,0]
dec2 = ib2o01wcs[:,1]
c = SkyCoord(ra=ra1*u.degree, dec=dec1*u.degree)
catalog = SkyCoord(ra=ra2*u.degree, dec=dec2*u.degree)
idx, d2d, d3d = c.match_to_catalog_sky(catalog)
#create an array of the c idx.
N=len(idx)
cnum=arange(0,N,1)
#make an array of cidx it's idx match and the distance between them
catdis=column_stack((cnum,idx,d2d))
#Keep only matches with a distance less than .5 as
catdisr=catdis[where(catdis[:,2] <= 0.000138889)]
#save new array to a text file
savetxt("catdisib2o02ib2o01.txt", catdisr, fmt='%f')
