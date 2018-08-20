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

mag1=ib2o05CMD[:,2]
mag2=ib2o06CMD[:,2]
mag3=ib2o08CMD[:,2]
mag4=ib2oa6CMD[:,2]
mag5=ib2oa7CMD[:,2]
mag6=ibop01CMD[:,2]
mag7=ibop02CMD[:,2]
mag8=ibop03CMD[:,2]
mag9=ibop04CMD[:,2]

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

ib2o05wcs=load("ib2o05wcs.npy")
ib2o06wcs=load("ib2o06wcs.npy")
ib2o08wcs=load("ib2o08wcs.npy")
ib2oa6wcs=load("ib2oa6wcs.npy")
ib2oa7wcs=load("ib2oa7wcs.npy")
ibop01wcs=load("ibop01wcs.npy")
ibop02wcs=load("ibop02wcs.npy")
ibop03wcs=load("ibop03wcs.npy")
ibop04wcs=load("ibop04wcs.npy")
#import catalog
catalog606=loadtxt("606catalog.txt")
N606=len(catalog606)
catalog814=zeros((N606,36))
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
#phot1=append(ib2o05wcs,ib2o05CMD, axis=1)
#phot2=append(ib2o06wcs,ib2o06CMD, axis=1)
#phot3=append(ib2o08wcs,ib2o08CMD, axis=1)
#phot4=append(ib2oa6wcs,ib2oa6CMD, axis=1)
#phot5=append(ib2oa7wcs,ib2oa7CMD, axis=1)
#phot6=append(ibop01wcs,ibop01CMD, axis=1)
#phot7=append(ibop02wcs,ibop02CMD, axis=1)
#phot8=append(ibop03wcs,ibop03CMD, axis=1)
#phot9=append(ibop04wcs,ibop04CMD, axis=1)

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
n1=len(catdisrn1)
n2=len(catdisrn2)
n3=len(catdisrn3)
n4=len(catdisrn4)
n5=len(catdisrn5)
n6=len(catdisrn6)
n7=len(catdisrn7)
n8=len(catdisrn8)
n9=len(catdisrn9)

numb1=arange(0,n1,1)
numb2=arange(0,n2,1)
numb3=arange(0,n3,1)
numb4=arange(0,n4,1)
numb5=arange(0,n5,1)
numb6=arange(0,n6,1)
numb7=arange(0,n7,1)
numb8=arange(0,n8,1)
numb9=arange(0,n9,1)


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

i12=intersect1d(catalogi1,catalogi2)
i13=intersect1d(catalogi1,catalogi3)
i14=intersect1d(catalogi1,catalogi4)
i15=intersect1d(catalogi1,catalogi5)
i16=intersect1d(catalogi1,catalogi6)
i17=intersect1d(catalogi1,catalogi7)
i18=intersect1d(catalogi1,catalogi8)
i19=intersect1d(catalogi1,catalogi9)
i23=intersect1d(catalogi2,catalogi3)
i24=intersect1d(catalogi2,catalogi4)
i25=intersect1d(catalogi2,catalogi5)
i26=intersect1d(catalogi2,catalogi6)
i27=intersect1d(catalogi2,catalogi7)
i28=intersect1d(catalogi2,catalogi8)
i29=intersect1d(catalogi2,catalogi9)
i34=intersect1d(catalogi3,catalogi4)
i35=intersect1d(catalogi3,catalogi5)
i36=intersect1d(catalogi3,catalogi6)
i37=intersect1d(catalogi3,catalogi7)
i38=intersect1d(catalogi3,catalogi8)
i39=intersect1d(catalogi3,catalogi9)
i45=intersect1d(catalogi4,catalogi5)
i46=intersect1d(catalogi4,catalogi6)
i47=intersect1d(catalogi4,catalogi7)
i48=intersect1d(catalogi4,catalogi8)
i49=intersect1d(catalogi4,catalogi9)
i56=intersect1d(catalogi5,catalogi6)
i57=intersect1d(catalogi5,catalogi7)
i58=intersect1d(catalogi5,catalogi8)
i59=intersect1d(catalogi5,catalogi9)
i67=intersect1d(catalogi6,catalogi7)
i68=intersect1d(catalogi6,catalogi8)
i69=intersect1d(catalogi6,catalogi9)
i78=intersect1d(catalogi7,catalogi8)
i79=intersect1d(catalogi7,catalogi9)
i89=intersect1d(catalogi8,catalogi9)
i11=intersect1d(catalogi1,catalogi1)
i22=intersect1d(catalogi2,catalogi2)
i33=intersect1d(catalogi3,catalogi3)
i44=intersect1d(catalogi4,catalogi4)
i55=intersect1d(catalogi5,catalogi5)
i66=intersect1d(catalogi6,catalogi6)
i77=intersect1d(catalogi7,catalogi7)
i88=intersect1d(catalogi8,catalogi8)
i99=intersect1d(catalogi9,catalogi9)


phot1=column_stack((catalogi1,imagei1,numb1))
phot2=column_stack((catalogi2,imagei2,numb2))
phot3=column_stack((catalogi3,imagei3,numb3))
phot4=column_stack((catalogi4,imagei4,numb4))
phot5=column_stack((catalogi5,imagei5,numb5))
phot6=column_stack((catalogi6,imagei6,numb6))
phot7=column_stack((catalogi7,imagei7,numb7))
phot8=column_stack((catalogi8,imagei8,numb8))
phot9=column_stack((catalogi9,imagei9,numb9))

immag1=[]
immag2=[]
immag3=[]
immag4=[]
immag5=[]
immag6=[]
immag7=[]
immag8=[]
immag9=[]

delcols1=[]
delcols2=[]
delcols3=[]
delcols4=[]
delcols5=[]
delcols6=[]
delcols7=[]
delcols8=[]
delcols9=[]
#for each set of intersections, find the image counterpart for the duplicated
for i in i12:
    x=where(phot1[:,0]==i)
    x2=where(phot2[:,0]==i)
    im=imagei1[x]
    im2=imagei2[x2]
    mag=mag1[im]
    magt=mag2[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols1.append(min(min(x)))
    delcols2.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i13:
    x=where(phot1[:,0]==i)
    x2=where(phot3[:,0]==i)
    im=imagei1[x]
    im2=imagei3[x2]
    mag=mag1[im]
    magt=mag3[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols1.append(min(min(x)))
    delcols3.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i14:
    x=where(phot1[:,0]==i)
    x2=where(phot4[:,0]==i)
    im=imagei1[x]
    im2=imagei4[x2]
    mag=mag1[im]
    magt=mag4[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols1.append(min(min(x)))
    delcols4.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i15:
    x=where(phot1[:,0]==i)
    x2=where(phot5[:,0]==i)
    im=imagei1[x]
    im2=imagei5[x2]
    mag=mag1[im]
    magt=mag5[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols1.append(min(min(x)))
    delcols5.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)

for i in i16:
    x=where(phot1[:,0]==i)
    x2=where(phot6[:,0]==i)
    im=imagei1[x]
    im2=imagei6[x2]
    mag=mag1[im]
    magt=mag6[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols1.append(min(min(x)))
    delcols6.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)

for i in i17:
    x=where(phot1[:,0]==i)
    x2=where(phot7[:,0]==i)
    im=imagei1[x]
    im2=imagei7[x2]
    mag=mag1[im]
    magt=mag7[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols1.append(min(min(x)))
    delcols7.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)

for i in i18:
    x=where(phot1[:,0]==i)
    x2=where(phot8[:,0]==i)
    im=imagei1[x]
    im2=imagei8[x2]
    mag=mag1[im]
    magt=mag8[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols1.append(min(min(x)))
    delcols8.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)

for i in i19:
    x=where(phot1[:,0]==i)
    x2=where(catalogi9==i)
    im=imagei1[x]
    im2=imagei9[x2]
    mag=mag1[im]
    magt=mag9[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols1.append(min(min(x)))
    delcols9.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)

for i in i23:
    x=where(phot2[:,0]==i)
    x2=where(phot3[:,0]==i)
    im=imagei2[x]
    im2=imagei3[x2]
    mag=mag2[im]
    magt=mag3[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols2.append(min(min(x)))
    delcols3.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i24:
    x=where(phot2[:,0]==i)
    x2=where(phot4[:,0]==i)
    im=imagei2[x]
    im2=imagei4[x2]
    mag=mag2[im]
    magt=mag4[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols2.append(min(min(x)))
    delcols4.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i25:
    x=where(phot2[:,0]==i)
    x2=where(phot5[:,0]==i)
    im=imagei2[x]
    im2=imagei5[x2]
    mag=mag2[im]
    magt=mag5[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols2.append(min(min(x)))
    delcols5.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i26:
    x=where(phot2[:,0]==i)
    x2=where(phot6[:,0]==i)
    im=imagei2[x]
    im2=imagei6[x2]
    mag=mag2[im]
    magt=mag6[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols2.append(min(min(x)))
    delcols6.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i27:
    x=where(phot2[:,0]==i)
    x2=where(phot7[:,0]==i)
    im=imagei2[x]
    im2=imagei7[x2]
    mag=mag2[im]
    magt=mag7[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols2.append(min(min(x)))
    delcols7.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i28:
    x=where(phot2[:,0]==i)
    x2=where(phot8[:,0]==i)
    im=imagei2[x]
    im2=imagei8[x2]
    mag=mag2[im]
    magt=mag8[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols2.append(min(min(x)))
    delcols8.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i29:
    x=where(phot2[:,0]==i)
    x2=where(catalogi9==i)
    im=imagei2[x]
    im2=imagei9[x2]
    mag=mag2[im]
    magt=mag9[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols2.append(min(min(x)))
    delcols9.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i34:
    x=where(phot3[:,0]==i)
    x2=where(phot4[:,0]==i)
    im=imagei3[x]
    im2=imagei4[x2]
    mag=mag3[im]
    magt=mag4[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols3.append(min(min(x)))
    delcols4.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i35:
    x=where(phot3[:,0]==i)
    x2=where(phot5[:,0]==i)
    im=imagei3[x]
    im2=imagei5[x2]
    mag=mag3[im]
    magt=mag5[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols3.append(min(min(x)))
    delcols5.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i36:
    x=where(phot3[:,0]==i)
    x2=where(phot6[:,0]==i)
    im=imagei3[x]
    im2=imagei6[x2]
    mag=mag3[im]
    magt=mag6[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols3.append(min(min(x)))
    delcols6.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i37:
    x=where(phot3[:,0]==i)
    x2=where(phot7[:,0]==i)
    im=imagei3[x]
    im2=imagei7[x2]
    mag=mag3[im]
    magt=mag7[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols3.append(min(min(x)))
    delcols7.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i38:
    x=where(phot3[:,0]==i)
    x2=where(phot8[:,0]==i)
    im=imagei3[x]
    im2=imagei8[x2]
    mag=mag3[im]
    magt=mag8[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols3.append(min(min(x)))
    delcols8.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i39:
    x=where(phot3[:,0]==i)
    x2=where(catalogi9==i)
    im=imagei3[x]
    im2=imagei9[x2]
    mag=mag3[im]
    magt=mag9[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols3.append(min(min(x)))
    delcols9.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i45:
    x=where(phot4[:,0]==i)
    x2=where(phot5[:,0]==i)
    im=imagei4[x]
    im2=imagei5[x2]
    mag=mag4[im]
    magt=mag5[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols4.append(min(min(x)))
    delcols5.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i46:
    x=where(phot4[:,0]==i)
    x2=where(phot6[:,0]==i)
    im=imagei4[x]
    im2=imagei6[x2]
    mag=mag4[im]
    magt=mag6[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols4.append(min(min(x)))
    delcols6.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i47:
    x=where(phot4[:,0]==i)
    x2=where(phot7[:,0]==i)
    im=imagei4[x]
    im2=imagei7[x2]
    mag=mag4[im]
    magt=mag7[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols4.append(min(min(x)))
    delcols7.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i48:
    x=where(phot4[:,0]==i)
    x2=where(phot8[:,0]==i)
    im=imagei4[x]
    im2=imagei8[x2]
    mag=mag4[im]
    magt=mag5[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols4.append(min(min(x)))
    delcols8.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i49:
    x=where(phot4[:,0]==i)
    x2=where(catalogi9==i)
    im=imagei4[x]
    im2=imagei9[x2]
    mag=mag4[im]
    magt=mag9[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols4.append(min(min(x)))
    delcols9.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i56:
    x=where(phot5[:,0]==i)
    x2=where(phot6[:,0]==i)
    im=imagei5[x]
    im2=imagei6[x2]
    mag=mag5[im]
    magt=mag6[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols5.append(min(min(x)))
    delcols6.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i57:
    x=where(phot5[:,0]==i)
    x2=where(phot7[:,0]==i)
    im=imagei5[x]
    im2=imagei7[x2]
    mag=mag5[im]
    magt=mag7[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols5.append(min(min(x)))
    delcols7.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i58:
    x=where(phot5[:,0]==i)
    x2=where(phot8[:,0]==i)
    im=imagei5[x]
    im2=imagei8[x2]
    mag=mag5[im]
    magt=mag8[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols5.append(min(min(x)))
    delcols8.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i59:
    x=where(phot5[:,0]==i)
    x2=where(catalogi9==i)
    im=imagei5[x]
    im2=imagei9[x2]
    mag=mag5[im]
    magt=mag9[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols5.append(min(min(x)))
    delcols9.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)

for i in i67:
    x=where(phot6[:,0]==i)
    x2=where(phot7[:,0]==i)
    im=imagei6[x]
    im2=imagei7[x2]
    mag=mag6[im]
    magt=mag7[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols6.append(min(min(x)))
    delcols7.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)

for i in i68:
    x=where(phot6[:,0]==i)
    x2=where(phot8[:,0]==i)
    im=imagei6[x]
    im2=imagei8[x2]
    mag=mag6[im]
    magt=mag8[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols6.append(min(min(x)))
    delcols8.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)

for i in i69:
    x=where(phot6[:,0]==i)
    x2=where(catalogi9==i)
    im=imagei6[x]
    im2=imagei9[x2]
    mag=mag6[im]
    magt=mag9[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols6.append(min(min(x)))
    delcols9.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)

for i in i78:
    x=where(phot7[:,0]==i)
    x2=where(phot8[:,0]==i)
    im=imagei7[x]
    im2=imagei8[x2]
    mag=mag7[im]
    magt=mag8[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols7.append(min(min(x)))
    delcols8.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)

for i in i79:
    x=where(phot7[:,0]==i)
    x2=where(catalogi9==i)
    im=imagei7[x]
    im2=imagei9[x2]
    mag=mag7[im]
    magt=mag9[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols7.append(min(min(x)))
    delcols9.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)

for i in i89:
    x=where(phot8[:,0]==i)
    x2=where(catalogi9==i)
    im=imagei8[x]
    im2=imagei9[x2]
    mag=mag8[im]
    magt=mag9[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols8.append(min(min(x)))
    delcols9.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
#check for the same source in the same list
for i in i11:
    x=where(phot1[:,0]==i)
    x2=where(catalogi1==i)
    im=imagei1[x]
    im2=imagei1[x2]
    mag=mag1[im]
    magt=mag1[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols1.append(min(min(x)))
    delcols1.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i22:
    x=where(phot2[:,0]==i)
    x2=where(catalogi2==i)
    im=imagei2[x]
    im2=imagei2[x2]
    mag=mag2[im]
    magt=mag2[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols2.append(min(min(x)))
    delcols2.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i33:
    x=where(phot3[:,0]==i)
    x2=where(catalogi3==i)
    im=imagei3[x]
    im2=imagei3[x2]
    mag=mag3[im]
    magt=mag3[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols3.append(min(min(x)))
    delcols3.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i44:
    x=where(phot4[:,0]==i)
    x2=where(catalogi4==i)
    im=imagei4[x]
    im2=imagei4[x2]
    mag=mag4[im]
    magt=mag4[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols4.append(min(min(x)))
    delcols4.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i55:
    x=where(phot5[:,0]==i)
    x2=where(catalogi5==i)
    im=imagei5[x]
    im2=imagei5[x2]
    mag=mag5[im]
    magt=mag5[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols5.append(min(min(x)))
    delcols5.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i66:
    x=where(phot6[:,0]==i)
    x2=where(catalogi6==i)
    im=imagei6[x]
    im2=imagei6[x2]
    mag=mag6[im]
    magt=mag6[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols6.append(min(min(x)))
    delcols6.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i77:
    x=where(phot7[:,0]==i)
    x2=where(catalogi7==i)
    im=imagei7[x]
    im2=imagei7[x2]
    mag=mag7[im]
    magt=mag7[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols7.append(min(min(x)))
    delcols7.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i88:
    x=where(phot8[:,0]==i)
    x2=where(catalogi8==i)
    im=imagei8[x]
    im2=imagei8[x2]
    mag=mag8[im]
    magt=mag8[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols8.append(min(min(x)))
    delcols8.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)
for i in i99:
    x=where(phot9[:,0]==i)
    x2=where(catalogi9==i)
    im=imagei9[x]
    im2=imagei9[x2]
    mag=mag9[im]
    magt=mag9[im2]
    #immag1.append(mag)
    #immag2.append(magt)
    delcols9.append(min(min(x)))
    delcols9.append(min(min(x2)))
    zerr=where(catalog814[i]==0)
    q=min(min(zerr))
    catalog814[i,q]=min(mag)
    catalog814[i,q+1]=min(magt)

savetxt("catalog814.txt",catalog814)

def avgvals(array):
    mmm=len(array)
    N=arange(0,mmm,1)
    for i in N:
        zerz=where(array[i]==0)
        q=min(min(zerz))
        qi=arange(0,q,1)
        num=min(min(zerz))
        avmag=0
        if q > 0:
            while q > 0:
                for p in qi:
                    avmag=avmag+array[i,p]
                    q=q-1
                    avgmag=avmag/num
            array[i,0]=avgmag

avgvals(catalog814)
savetxt("814catalog.txt",catalog814,fmt="%f")
cat814=array(catalog814[:,0],ndmin=2)
catt814=transpose(cat814)

udelcols1=unique(delcols1)
udelcols2=unique(delcols2)
udelcols3=unique(delcols3)
udelcols4=unique(delcols4)
udelcols5=unique(delcols5)
udelcols6=unique(delcols6)
udelcols7=unique(delcols7)
udelcols8=unique(delcols8)
udelcols9=unique(delcols9)

for i in udelcols1:
    x=where(phot1[:,2]==i)
    phot1=delete(phot1,x, 0)
for i in udelcols2:
    x=where(phot2[:,2]==i)
    phot2=delete(phot2,x, 0)
for i in udelcols3:
    x=where(phot3[:,2]==i)
    phot3=delete(phot3,x, 0)
for i in udelcols4:
    x=where(phot4[:,2]==i)
    phot4=delete(phot4,x, 0)
for i in udelcols5:
    x=where(phot5[:,2]==i)
    phot5=delete(phot5,x, 0)
for i in udelcols6:
    x=where(phot6[:,2]==i)
    phot6=delete(phot6,x, 0)
for i in udelcols7:
    x=where(phot7[:,2]==i)
    phot7=delete(phot7,x, 0)
for i in udelcols8:
    x=where(phot8[:,2]==i)
    phot8=delete(phot8,x, 0)
for i in udelcols9:
    x=where(phot9[:,2]==i)
    phot9=delete(phot9,x, 0)

cati1=phot1[:,0]
cati2=phot2[:,0]
cati3=phot3[:,0]
cati4=phot4[:,0]
cati5=phot5[:,0]
cati6=phot6[:,0]
cati7=phot7[:,0]
cati8=phot8[:,0]
cati9=phot9[:,0]

for i in cati1:
    x=where(cati1==i)
    im=phot1[x,1]
    mag=mag1[im]
    catt814[i,0]=min(mag)
for i in cati2:
    x=where(cati2==i)
    im=phot2[x,1]
    mag=mag2[im]
    catt814[i,0]=min(mag)
for i in cati3:
    x=where(cati3==i)
    im=phot3[x,1]
    mag=mag3[im]
    catt814[i,0]=min(mag)
for i in cati4:
    x=where(cati4==i)
    im=phot4[x,1]
    mag=mag4[im]
    catt814[i,0]=min(mag)
for i in cati5:
    x=where(cati5==i)
    im=phot5[x,1]
    mag=mag5[im]
    catt814[i,0]=min(mag)
for i in cati6:
    x=where(cati6==i)
    im=phot6[x,1]
    mag=mag6[im]
    catt814[i,0]=min(mag)
for i in cati7:
    x=where(cati7==i)
    im=phot7[x,1]
    mag=mag7[im]
    catt814[i,0]=min(mag)
for i in cati8:
    x=where(cati8==i)
    im=phot8[x,1]
    mag=mag8[im]
    catt814[i,0]=min(mag)
for i in cati9:
    x=where(cati9==i)
    im=phot9[x,1]
    mag=mag9[im]
    catt814[i,0]=min(mag)


cat6819=append(catalog606,catt814,axis=1)
savetxt("6819catalog.txt",cat6819,fmt="%f")
