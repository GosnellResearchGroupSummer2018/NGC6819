"""catmat3.py a program to match sources between different source catalogs"""
#import modules
from astropy.coordinates import SkyCoord
from astropy import units as u
from numpy import *
#import photometry data
catalist2=loadtxt("catalist2.txt")
catalist1=loadtxt("catalist1.txt")
catalogpos1=column_stack((catalist1[:,0],catalist1[:,1]))
catalogpos2=column_stack((catalist2[:,0],catalist2[:,1]))
ra1 = catalist1[:,0]
#second column as dec
dec1 = catalist1[:,1]
#do it with the other data
ra2 = catalist2[:,0]
dec2 = catalist2[:,1]
catalo1 = SkyCoord(ra=ra1*u.degree, dec=dec1*u.degree)
catalo2 = SkyCoord(ra=ra2*u.degree, dec=dec2*u.degree)
cidx, d2d, d3d = catalo2.match_to_catalog_sky(catalo1)
#create an array with all the data
#ib2o04phot=append(ib2o04wcs,ib2o04CMD, axis=1)
#ib2o03phot=append(ib2o03wcs,ib2o03CMD, axis=1)
#create an array of the c tidx.
N=len(cidx)
idx=arange(0,N,1)
#make an array of odx it's idx match and the distance between them
d2dv=d2d.value
catdis=column_stack((idx,cidx,d2dv))
#Keep only matches with a distance less than .5 as
catdisr=catdis[where(catdis[:,2] <= 0.000138889)]
#save new array to a text file
CN=len(catdisr)
CNa=arange(0,CN,1)
catdisrn=column_stack((CNa,catdisr))
savetxt("catdis12.txt", catdisrn, fmt='%d %d %d %f')
#what am i doing
imagei = asarray(catdisrn[:,1],dtype=int)
catalogi = asarray(catdisrn[:,2],dtype=int)
matchi = asarray(catdisrn[:,0],dtype=int)
cat1mags=catalist1[:,4]
cat2mags=catalist2[:,4]
catmag=[]
immag=[]
matchmag=[]
for i in imagei:
    mag = cat2mags[i]
    catmag.append(mag)
    delete(catalist2,i, 0)
for i in catalogi:
    mag = cat1mags[i]
    immag.append(mag)
    delete(catalist1,i, 0)
for i in matchi:
    mag=(catmag[i]+immag[i])/2
    matchmag.append(mag)
nml=len(matchmag)
matchwcs=zeros((nml,2))
zeros=zeros((nml,2))
imwcs=empty((nml,2))
catwcs=empty((nml,2))
x=0
y=0
for i in imagei:
    wcs = catalogpos2[i]
    imwcs[x]=wcs
    x=x+1
for i in catalogi:
    wcs = catalogpos1[i]
    catwcs[y]=wcs
    y=y+1
for i in matchi:
    ra=(imwcs[i,0]+catwcs[i,0])/2
    dec=(imwcs[i,1]+catwcs[i,1])/2
    matchwcs[i]=array((ra,dec))
nmaga=array(matchmag,ndmin=2)
anmag=transpose(nmaga)
share0102=append(matchwcs,zeros, axis=1)
shared0102=append(share0102,anmag,axis=1)
#add the shared values to the photometry list
catalist3=concatenate((catalist1,catalist2,shared0102),axis=0)
catalogpos3=array((catalist3[:,0],catalist3[:,1]))
savetxt("606catalog.txt", catalist3, fmt='%f')
