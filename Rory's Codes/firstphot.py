"""firstphot.py a photometry program by rory lowe as part of the Gosnell Research Group attempting to use photutils to analyze HST data of NGC6819"""
#remove background-is this even necessary given that the background on these images is significanty lower than the data.
#import modules
from photutils import make_source_mask
#bring the data in
data = "/Volumes/64FLASH/astro/MAST_2018-06-25T2014/HST/ib2o03020/ib2o03020_drc.fits"
#define the masking function
mask = make_source_mask(data, snr=2, npixels=5, dilate_size=11)
#error on this line ufunc 'isfinite' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
#get results from masking function
mean, median, std = sigma_clipped_stats(data, sigma=3.0, mask=mask)
#print results
print(mean, median, std)
