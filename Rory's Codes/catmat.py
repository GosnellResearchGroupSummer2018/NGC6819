"""catmat.py a program to match sources between different source catalogs"""
#import modules
from astropy.coordinates import SkyCoord
from astropy import units as u
from numpy import *
#import position wcs data
ibop04wcs = load("ibop04wcs.npy")
#define first column as ra
ra1 = ibop04wcs[:,0]
#second column as dec
dec1 = ibop04wcs[:,1]
#do it with the other data
ib2o01wcs = load("ib2o01wcs.npy")
ra2 = ib2o01wcs[:,0]
dec2 = ib2o01wcs[:,1]
c = SkyCoord(ra=ra1*u.degree, dec=dec1*u.degree)
catalog = SkyCoord(ra=ra2*u.degree, dec=dec2*u.degree)
idx, d2d, d3d = c.match_to_catalog_sky(catalog)
