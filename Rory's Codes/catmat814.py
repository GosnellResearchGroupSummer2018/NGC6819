"""catmat814.py a program to match all 814 sources with each other and the 606 catalog"""
#import modules
from astropy.coordinates import SkyCoord
from astropy import units as u
from numpy import *
#import photometry data
ib2o05CMD=loadtxt('/Volumes/64FLASH/dolphotresults/ib2o05/CMD.txt')
ib2o06CMD=loadtxt('/Volumes/64FLASH/dolphotresults/ib2o06/CMD.txt')
ib2o08CMD=loadtxt('/Volumes/64FLASH/dolphotresults/ib2o08/CMD.txt')
ib2oa6CMD=loadtxt('/Volumes/64FLASH/dolphotresults/ib2oa6/CMD.txt')
ib2oa7CMD=loadtxt('/Volumes/64FLASH/dolphotresults/ib2oa7/CMD.txt')
ibop01CMD=loadtxt('/Volumes/64FLASH/dolphotresults/ibop01/CMD.txt')
ibop02CMD=loadtxt('/Volumes/64FLASH/dolphotresults/ibop02/CMD.txt')
ibop03CMD=loadtxt('/Volumes/64FLASH/dolphotresults/ibop03/CMD.txt')
ibop04CMD=loadtxt('/Volumes/64FLASH/dolphotresults/ibop04/CMD.txt')

#import position wcs data
ra1,dec1=transpose(load("ib2o05wcs.npy"))
ra2,dec2=transpose(load("ib2o06wcs.npy"))
ra3,dec3=transpose(load("ib2o08wcs.npy"))
ra4,dec4=transpose(load("ib2oa6wcs.npy"))
ra5,dec5=transpose(load("ib2oa7wcs.npy"))
ra6,dec6=transpose(load("ibop01wcs.npy"))
ra7,dec7=transpose(load("ibop02wcs.npy"))
ra8,dec8=transpose(load("ibop03wcs.npy"))
ra9,dec9=transpose(load("ibop04wcs.npy"))
#import catalog
catalog606=load("606catalog.txt")
cra = catalog606[:,0]
#second column as dec
cdec = catalog606[:,1]
#run skycoords on everything
catalog = SkyCoord(ra=cra*u.degree, dec=cdec*u.degree)
ib2o05 = SkyCoord(ra=ra1*u.degree, dec=dec1*u.degree)
ib2o06 = SkyCoord(ra=ra2*u.degree, dec=dec2*u.degree)
ib2o08 = SkyCoord(ra=ra3*u.degree, dec=dec3*u.degree)
ib2oa6 = SkyCoord(ra=ra4*u.degree, dec=dec4*u.degree)
ib2oa7 = SkyCoord(ra=ra5*u.degree, dec=dec5*u.degree)
ibop01 = SkyCoord(ra=ra6*u.degree, dec=dec6*u.degree)
ibop02 = SkyCoord(ra=ra7*u.degree, dec=dec7*u.degree)
ibop03 = SkyCoord(ra=ra8*u.degree, dec=dec8*u.degree)
ibop04 = SkyCoord(ra=ra9*u.degree, dec=dec9*u.degree)
#do a catalog match on everything
cidx1, d2d1, d3d1 = ib2o05.match_to_catalog_sky(catalog)
cidx2, d2d2, d3d2 = ib2o06.match_to_catalog_sky(catalog)
cidx3, d2d3, d3d3 = ib2o08.match_to_catalog_sky(catalog)
cidx4, d2d4, d3d4 = ib2oa6.match_to_catalog_sky(catalog)
cidx5, d2d5, d3d5 = ib2oa7.match_to_catalog_sky(catalog)
cidx6, d2d6, d3d6 = ibop01.match_to_catalog_sky(catalog)
cidx7, d2d7, d3d7 = ibop02.match_to_catalog_sky(catalog)
cidx8, d2d8, d3d8 = ibop03.match_to_catalog_sky(catalog)
cidx9, d2d9, d3d9 = ibop04.match_to_catalog_sky(catalog)

#create an array with all the data
ib2o05phot=append(ib2o05wcs,ib2o05CMD, axis=1)
ib2o06phot=append(ib2o06wcs,ib2o06CMD, axis=1)
ib2o08phot=append(ib2o08wcs,ib2o08CMD, axis=1)
ib2oa6phot=append(ib2oa6wcs,ib2oa6CMD, axis=1)
ib2oa7phot=append(ib2oa7wcs,ib2oa7CMD, axis=1)
ibop01phot=append(ibop01wcs,ibop01CMD, axis=1)
ibop02phot=append(ibop02wcs,ibop02CMD, axis=1)
ibop03phot=append(ibop03wcs,ibop03CMD, axis=1)
ibop04phot=append(ibop04wcs,ibop04CMD, axis=1)

#create an array of the cidx.
N1=len(cidx1)
N2=len(cidx2)
N3=len(cidx3)
N4=len(cidx4)
N5=len(cidx5)
N6=len(cidx6)
N7=len(cidx7)
N8=len(cidx8)
N9=len(cidx9)

idx1=arange(0,N1,1)
idx2=arange(0,N2,1)
idx3=arange(0,N3,1)
idx4=arange(0,N4,1)
idx5=arange(0,N5,1)
idx6=arange(0,N6,1)
idx7=arange(0,N7,1)
idx8=arange(0,N8,1)
idx9=arange(0,N9,1)

#make an array of odx it's idx match and the distance between them
d2dv1=d2d1.value
d2dv2=d2d2.value
d2dv3=d2d3.value
d2dv4=d2d4.value
d2dv5=d2d5.value
d2dv6=d2d6.value
d2dv7=d2d7.value
d2dv8=d2d8.value
d2dv9=d2d9.value

catdis1=column_stack((idx1,cidx1,d2dv1))
catdis2=column_stack((idx2,cidx2,d2dv2))
catdis3=column_stack((idx3,cidx3,d2dv3))
catdis4=column_stack((idx4,cidx4,d2dv4))
catdis5=column_stack((idx5,cidx5,d2dv5))
catdis6=column_stack((idx6,cidx6,d2dv6))
catdis7=column_stack((idx7,cidx7,d2dv7))
catdis8=column_stack((idx8,cidx8,d2dv8))
catdis9=column_stack((idx9,cidx9,d2dv9))

#Keep only matches with a distance less than .5 as
catdisr1=catdis1[where(catdis1[:,2] <= 0.000138889)]
catdisr2=catdis2[where(catdis2[:,2] <= 0.000138889)]
catdisr3=catdis3[where(catdis3[:,2] <= 0.000138889)]
catdisr4=catdis4[where(catdis4[:,2] <= 0.000138889)]
catdisr5=catdis5[where(catdis5[:,2] <= 0.000138889)]
catdisr6=catdis6[where(catdis6[:,2] <= 0.000138889)]
catdisr7=catdis7[where(catdis7[:,2] <= 0.000138889)]
catdisr8=catdis8[where(catdis8[:,2] <= 0.000138889)]
catdisr9=catdis9[where(catdis9[:,2] <= 0.000138889)]

#save new array to a text file
CN1=len(catdisr1)
CN2=len(catdisr2)
CN3=len(catdisr3)
CN4=len(catdisr4)
CN5=len(catdisr5)
CN6=len(catdisr6)
CN7=len(catdisr7)
CN8=len(catdisr8)
CN9=len(catdisr9)

CNa1=arange(0,CN1,1)
CNa2=arange(0,CN2,1)
CNa3=arange(0,CN3,1)
CNa4=arange(0,CN4,1)
CNa5=arange(0,CN5,1)
CNa6=arange(0,CN6,1)
CNa7=arange(0,CN7,1)
CNa8=arange(0,CN8,1)
CNa9=arange(0,CN9,1)

catdisrn1=column_stack((CNa1,catdisr1))
catdisrn2=column_stack((CNa2,catdisr2))
catdisrn3=column_stack((CNa3,catdisr3))
catdisrn4=column_stack((CNa4,catdisr4))
catdisrn5=column_stack((CNa5,catdisr5))
catdisrn6=column_stack((CNa6,catdisr6))
catdisrn7=column_stack((CNa7,catdisr7))
catdisrn8=column_stack((CNa8,catdisr8))
catdisrn9=column_stack((CNa9,catdisr9))

savetxt("catdis1.txt", catdisrn1, fmt='%d %d %d %f')
savetxt("catdis2.txt", catdisrn2, fmt='%d %d %d %f')
savetxt("catdis3.txt", catdisrn3, fmt='%d %d %d %f')
savetxt("catdis4.txt", catdisrn4, fmt='%d %d %d %f')
savetxt("catdis5.txt", catdisrn5, fmt='%d %d %d %f')
savetxt("catdis6.txt", catdisrn6, fmt='%d %d %d %f')
savetxt("catdis7.txt", catdisrn7, fmt='%d %d %d %f')
savetxt("catdis8.txt", catdisrn8, fmt='%d %d %d %f')
savetxt("catdis9.txt", catdisrn9, fmt='%d %d %d %f')

#what am i doing
imagei1 = asarray(catdisrn1[:,1],dtype=int)
imagei2 = asarray(catdisrn2[:,1],dtype=int)
imagei3 = asarray(catdisrn3[:,1],dtype=int)
imagei4 = asarray(catdisrn4[:,1],dtype=int)
imagei5 = asarray(catdisrn5[:,1],dtype=int)
imagei6 = asarray(catdisrn6[:,1],dtype=int)
imagei7 = asarray(catdisrn7[:,1],dtype=int)
imagei8 = asarray(catdisrn8[:,1],dtype=int)
imagei9 = asarray(catdisrn9[:,1],dtype=int)

catalogi1 = asarray(catdisrn1[:,2],dtype=int)
catalogi2 = asarray(catdisrn2[:,2],dtype=int)
catalogi3 = asarray(catdisrn3[:,2],dtype=int)
catalogi4 = asarray(catdisrn4[:,2],dtype=int)
catalogi5 = asarray(catdisrn5[:,2],dtype=int)
catalogi6 = asarray(catdisrn6[:,2],dtype=int)
catalogi7 = asarray(catdisrn7[:,2],dtype=int)
catalogi8 = asarray(catdisrn8[:,2],dtype=int)
catalogi9 = asarray(catdisrn9[:,2],dtype=int)

matchi = asarray(catdisrn[:,0],dtype=int)
ib2o04mags=loadtxt('/Volumes/64FLASH/dolphotresults/ib2o04/mags.txt')
ib2o03mags=loadtxt('/Volumes/64FLASH/dolphotresults/ib2o03/mags.txt')
catmag=[]
immag=[]
matchmag=[]
for i in imagei:
    mag = ib2o04mags[i,2]
    immag.append(mag)
    delete(ib2o04phot,i, 0)
for i in catalogi:
    mag = ib2o03mags[i,2]
    catmag.append(mag)
    delete(ib2o03phot,i, 0)
for i in matchi:
    mag=(immag[i]+catmag[i])/2
    matchmag.append(mag)
nml=len(matchmag)
matchwcs=zeros((nml,2))
zeros=zeros((nml,2))
imwcs=empty((nml,2))
catwcs=empty((nml,2))
x=0
y=0
for i in imagei:
    wcs = ib2o04wcs[i]
    catwcs[x]=wcs
    x=x+1
for i in catalogi:
    wcs = ib2o03wcs[i]
    imwcs[y]=wcs
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
catalist2=concatenate((ib2o03phot,ib2o04phot,shared0102),axis=0)
savetxt("catalist2.txt", catalist2, fmt='%f')"""
