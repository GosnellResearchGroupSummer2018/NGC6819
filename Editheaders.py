from astropy.io import fits

hdulist = fits.open("ib2o01020_drc.fits", header=True)
hdu = hdulist[0]

header["the header"] = "the value or string"



hdu.writeto('newheader.fits', data, header, overwrite=True)
