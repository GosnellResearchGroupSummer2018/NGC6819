from astropy.io import fits

data, header = fits.getdata("ib2o01020_drc.fits", header=True)

header["READNSEA"] = 3.0300000E+00
header["READNSEB"] = 3.1300001E+00
header["READNSEC"] = 3.0799999E+00
header["READNSED"] = 3.1800001E+00
header["NCOMBINE"] = 5
header["FILETYPE"] = 'SCI'
header["TELESCOP"] = 'HST'
header["INSTRUME"] = 'WFC3'
header["DETECTOR"] = 'UVIS'
header["APERTURE"] = 'UVIS-CENTER'
#header[""] =


fits.writeto('newheader.fits', data, header, overwrite=True)
