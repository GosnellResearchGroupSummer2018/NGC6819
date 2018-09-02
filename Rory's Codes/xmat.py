"""xmat.py a program to match x-rays to sources"""
#import modules
from astropy.coordinates import SkyCoord
from astropy import units as u
from numpy import *
#import photometry data
source,rah,ram,ras,decd,decm,decs=loadtxt('/Users/rorylowe/Desktop/gitrepos/NGC6819/xraysourcecoords.txt',usecols=(0,1,2,3,4,5,6),skiprows=1,unpack=True)
catalog=loadtxt("6819matchedcatalog.txt")
xra=rah*15+ram*.25+ras*(1/240)
xdec=decd+decm*(1/60)+decs*(1/3600)
xa=column_stack((xra,xdec))
savetxt("xa.txt",xa)
#define first column as ra
cra = catalog[:,0]
#second column as dec
cdec = catalog[:,1]
xrays = SkyCoord(ra=xra*u.degree, dec=xdec*u.degree)
catalogs = SkyCoord(ra=cra*u.degree, dec=cdec*u.degree)
cidx, d2d, d3d = xrays.match_to_catalog_sky(catalogs)
#create an array of the c tidx.
N=len(cidx)
idx=arange(1,N+1,1)
#make an array of odx it's idx match and the distance between them
d2dv=d2d.value
catdis=column_stack((idx,cidx,d2dv))
#Keep only matches with a distance less than 2 as
catdisr=catdis[where(catdis[:,2] <= 0.000555556)]
#save new array to a text file
CN=len(catdisr)
CNa=arange(0,CN,1)
catdisrn=column_stack((CNa,catdisr))
savetxt("catdisxc.txt", catdisrn, fmt='%d %d %d %f')
nn=len(catalog)
xsa=zeros((nn,1))
for i in CNa:
    cn=int(catdisr[i,1])
    xn=catdisr[i,0]
    xsa[cn]=xn
catalogwx=append(catalog,xsa, axis=1)
savetxt("6819xmatchedcat.txt", catalogwx)
