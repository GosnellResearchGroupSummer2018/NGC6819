"""catmat3.py a program to match sources between different source catalogs"""
#import modules
from astropy.coordinates import SkyCoord
from astropy import units as u
from numpy import *
#import photometry data
catalist2=loadtxt("catalist2.txt")
catalist1=loadtxt("catalist1.txt")
catalogpos1=array((catalist1[:,0],catalist1[:,1]))
catalogpos2=array((catalist2[:,0],catalist2[:,1]))
ra1 = catalogpos1[:,0]
#second column as dec
dec1 = catalogpos1[:,1]
#do it with the other data
ra2 = catalogpos2[:,0]
dec2 = catalogpos2[:,1]
catalo1 = SkyCoord(ra=ra1*u.degree, dec=dec1*u.degree)
catalo2 = SkyCoord(ra=ra2*u.degree, dec=dec2*u.degree)
idx2, d2d, d3d = ib2o03.match_to_catalog_sky(cata2)
#create an array with all the data
#ib2o04phot=append(ib2o04wcs,ib2o04CMD, axis=1)
#ib2o03phot=append(ib2o03wcs,ib2o03CMD, axis=1)
#create an array of the c tidx.
N=len(idx1)
idx1=arange(0,N,1)
#make an array of odx it's idx match and the distance between them
d2dv=d2d.value
catdis=column_stack((idx1,idx2,d2dv))
#Keep only matches with a distance less than .5 as
catdisr=catdis[where(catdis[:,2] <= 0.000138889)]
#save new array to a text file
CN=len(catdisr)
CNa=arange(0,CN,1)
catdisrn=column_stack((CNa,catdisr))
savetxt("catdis12.txt", catdisrn, fmt='%d %d %d %f')
#what am i doing
o = asarray(catdisrn[:,1],dtype=int)
t = asarray(catdisrn[:,2],dtype=int)
n = asarray(catdisrn[:,0],dtype=int)
cat1mags=catalist1[:,4]
cat2mags=catalist2[:,4]
tmag=[]
omag=[]
nmag=[]
for i in o:
    mag = cat1mags[i,2]
    tmag.append(mag)
    delete(catalist1,i, 0)
for i in t:
    mag = cat2mags[i,2]
    omag.append(mag)
    delete(catalist2,i, 0)
for i in n:
    mag=(tmag[i]+omag[i])/2
    nmag.append(mag)
nml=len(nmag)
nwcs=zeros((nml,2))
zeros=zeros((nml,2))
owcs=empty((nml,2))
twcs=empty((nml,2))
x=0
y=0
for i in o:
    wcs = catalogpos1[i]
    twcs[x]=wcs
    x=x+1
for i in t:
    wcs = catalogpos2[i]
    owcs[y]=wcs
    y=y+1
for i in n:
    ra=(owcs[i,0]+twcs[i,0])/2
    dec=(owcs[i,1]+twcs[i,1])/2
    nwcs[i]=array((ra,dec))
nmaga=array(nmag,ndmin=2)
anmag=transpose(nmaga)
share0102=append(nwcs,zeros, axis=1)
shared0102=append(share0102,anmag,axis=1)
#add the shared values to the photometry list
catalist3=concatenate((catalist1,catalist2,shared0102),axis=0)
catalogpos3=array((catalist3[:,0],catalist3[:,1]))
savetxt("catalist3.txt", catalist3, fmt='%f')
