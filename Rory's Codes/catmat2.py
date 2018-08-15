"""catmat.py a program to match sources between different source catalogs"""
#import modules
from astropy.coordinates import SkyCoord
from astropy import units as u
from numpy import *
#import photometry data
ib2o04CMD=loadtxt('/Volumes/64FLASH/dolphotresults/ib2o04/CMD.txt')
ib2o03CMD=loadtxt('/Volumes/64FLASH/dolphotresults/ib2o03/CMD.txt')
#import position wcs data
ib2o04wcs = load("ib2o04wcs.npy")
#define first column as ra
ra1 = ib2o04wcs[:,0]
#second column as dec
dec1 = ib2o04wcs[:,1]
#do it with the other data
ib2o03wcs = load("ib2o03wcs.npy")
ra2 = ib2o03wcs[:,0]
dec2 = ib2o03wcs[:,1]
ib2o03 = SkyCoord(ra=ra1*u.degree, dec=dec1*u.degree)
ib2o04 = SkyCoord(ra=ra2*u.degree, dec=dec2*u.degree)
tidx, d2d, d3d = ib2o03.match_to_catalog_sky(ib2o04)
#create an array with all the data
ib2o04phot=append(ib2o04wcs,ib2o04CMD, axis=1)
ib2o03phot=append(ib2o03wcs,ib2o03CMD, axis=1)
#create an array of the c tidx.
N=len(tidx)
oidx=arange(0,N,1)
#make an array of odx it's idx match and the distance between them
d2dv=d2d.value
catdis=column_stack((oidx,tidx,d2dv))
#Keep only matches with a distance less than .5 as
catdisr=catdis[where(catdis[:,2] <= 0.000138889)]
#save new array to a text file
CN=len(catdisr)
CNa=arange(0,CN,1)
catdisrn=column_stack((CNa,catdisr))
savetxt("catdisib2o04ib2o03.txt", catdisrn, fmt='%d %d %d %f')
#what am i doing
o = asarray(catdisrn[:,1],dtype=int)
t = asarray(catdisrn[:,2],dtype=int)
n = asarray(catdisrn[:,0],dtype=int)
ib2o04mags=loadtxt('/Volumes/64FLASH/dolphotresults/ib2o04/mags.txt')
ib2o03mags=loadtxt('/Volumes/64FLASH/dolphotresults/ib2o03/mags.txt')
tmag=[]
omag=[]
nmag=[]
for i in o:
    mag = ib2o04mags[i,2]
    tmag.append(mag)
    delete(ib2o04phot,i, 0)
for i in t:
    mag = ib2o03mags[i,2]
    omag.append(mag)
    delete(ib2o03phot,i, 0)
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
    wcs = ib2o04wcs[i]
    twcs[x]=wcs
    x=x+1
for i in t:
    wcs = ib2o03wcs[i]
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
catalist2=concatenate((ib2o03phot,ib2o04phot,shared0102),axis=0)
catalogpos2=array((catalist2[:,0],catalist2[:,1]))
savetxt("catalist2.txt", catalist2, fmt='%f')
