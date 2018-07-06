"""samap.py an aperture photometry program using sample images"""
from photutils import make_source_mask
from astropy.stats import sigma_clipped_stats
from pylab import *
from scipy import *
from numpy import *
from photutils import datasets
id, xcentroid, ycentroid, sharpness, roundness1, roundness2, npix, sky, peak, flux, mag = load('samsdout.npy')
