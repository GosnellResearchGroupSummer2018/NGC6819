"""catmat.py a program to match sources between different source catalogs"""
#import modules
from astropy.coordinates import SkyCoord
from astropy import units as u
from numpy import *
#import photometry data
ib2o02CMD=loadtxt('/Volumes/64FLASH/dolphotresults/ib2o02/CMD.txt')
ib2o01CMD=loadtxt('/Volumes/64FLASH/dolphotresults/ib2o01/CMD.txt')
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
"""ra2=ara2.value
ra1=ara1.value
dec2=adec2.value
dec1=adec1.value"""
ib2o02 = SkyCoord(ra=ra1*u.degree, dec=dec1*u.degree)
ib2o01 = SkyCoord(ra=ra2*u.degree, dec=dec2*u.degree)
cidx, d2d, d3d = ib2o01.match_to_catalog_sky(ib2o02)
#create an array with all the data
ib2o02phot=append(ib2o02wcs,ib2o02CMD, axis=1)
ib2o01phot=append(ib2o01wcs,ib2o01CMD, axis=1)
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
savetxt("catdisib2o02ib2o01.txt", catdisrn, fmt='%d %d %d %f')
#what am i doing
imagei = asarray(catdisrn[:,1],dtype=int)
catalogi = asarray(catdisrn[:,2],dtype=int)
matchi = asarray(catdisrn[:,0],dtype=int)
photo01=column_stack((catalogi,imagei))
ib2o02mags=loadtxt('/Volumes/64FLASH/dolphotresults/ib2o02/mags.txt')
ib2o01mags=loadtxt('/Volumes/64FLASH/dolphotresults/ib2o01/mags.txt')
catmag=[]
immag=[]
matchmag=[]
for i in imagei:
    x=where(imagei==i)
    c=catalogi[x]
    cmag = ib2o02mags[c,2]
    mag = ib2o01mags[i,2]
    immag.append(mag)
    catmag.append(cmag)
    ib2o02phot=delete(ib2o02phot,c, 0)
    ib2o01phot=delete(ib2o01phot,i, 0)
#for i in catalogi:
#    x=where(catalogi==i)
#    c=imagei[x]
#    mag = ib2o01mags[i,2]
#    immag.append(mag)
#    ib2o01phot=delete(ib2o01phot,c, 0)
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
    wcs = ib2o02wcs[i]
    catwcs[x]=wcs
    x=x+1
for i in catalogi:
    wcs = ib2o01wcs[i]
    imwcs[y]=wcs
    y=y+1
for i in matchi:
    ra=(imwcs[i,0]+catwcs[i,0])/2
    dec=(imwcs[i,1]+catwcs[i,1])/2
    matchwcs[i]=array((ra,dec))
nmaga=array(matchmag,ndmin=2)
anmag=transpose(nmaga)
share0102=append(matchwcs,zeros, axis=1)
shared0102=append(share0102,nmaga,axis=1)
#add the shared values to the photometry list
catalist1=concatenate((ib2o01phot,ib2o02phot,shared0102),axis=0)
catalogpos1=array((catalist1[:,0],catalist1[:,1]))
savetxt("catalist1.txt", catalist1, fmt='%f')
