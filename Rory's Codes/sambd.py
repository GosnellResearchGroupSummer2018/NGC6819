"""sambd.py a background detection program using sample images
It uses the source masking means of background detection"""
from photutils import make_source_mask
from astropy.stats import sigma_clipped_stats
from pylab import *
from scipy import *
from numpy import *
from photutils import datasets
#bring the data in.
#I have tried to use one of the .fits hubble images here, but it returns the ufunc
#'isfinite' error explained below. I think it is an issue with formatting,
#but am not sure right now (and am not super concerned as this is just to
#learn how to do photometry in general)
#i am now using the make_100gaussians_image from photutils.datasets
#that they utilize in the readthedocs tutorial.
#the data that wouldn't work: #data = "/Volumes/64FLASH/astro/MAST_2018-06-25T2014/HST/ib2o03020/ib2o03020_drc.fits"
#next three lines from Thom's photometry program: solves fits read issues
from astropy.io import fits
hdu = fits.open("/Volumes/64FLASH/astro/MAST_2018-06-25T2014/HST/ib2o03020/ib2o03020_drc.fits")[1]
data = hdu.data[2500:3200, 2500:3200] #This image is 5644x5895 piels, and I want to restrict my search to the very small section in the center because the edges of these images are noisy and this code is optimized to work on smaller images.
save("data.npy", data)
#data = datasets.load_star_image()
#define the mask function
#the mask function defines which points will not be considered as part of the background.
#The idea here is that by removing all the sources the background can be understood to be everything else
#snr is the signal to noise ratio above the background a pixel value must be to be considered to be due to a source for our mask
#npixels defines how many contiguous pixels must be above the defined snr threshold to be considered a source (just one pixel whose value lies above the snr threshold on its own would not be considered a source)
#dilate_size defines the pixel size of a box that will be marked off around each sources
#the listed size is the dimension of one side of the box.
mask = make_source_mask(data, snr=2, npixels=5, dilate_size=11)
#error on this line ufunc 'isfinite' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
#get results from masking function
#get the data from the masked image
#sigma_clipped_stats is from astropy and it goes through the image and finds the mean median and standard deviation of the pixel values.
#It discards data above or below a certain standard deviation (I let it use its default value of 3.0 since that is the same value as was used in the photutils tutorial)
#this is not redundant with the make_source_mask because make_source_mask requires that pixels must be both above a certain snr and also contiguous with other pixels above that snr to be masked
#so pixels whose values are alone at an extreme value (or that have less than 5 neighbors at a similarly extreme value) will be kept with the source mask but can be eliminated with the sigma clipping of sigma_clipped_stats
#the mask parameter here simply defines the array of values for sigma_clipped_stats to ignore in its calculation of mean median and std
#I set up this masking array in the previous line with make_source_mask and it is conveninetly named mask.
mean, median, std = sigma_clipped_stats(data, mask=mask)
#print results
print (mean, median, std)
#put the results into a text file to use in a future program
savetxt('sambdout.txt', ["%f  %f  %f" % (mean, median, std)], fmt='%s')
