from numpy import *

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
cat814test=loadtxt("814cattest.txt")
avgvals(cat814test)
savetxt("cat814test.txt",cat814test)
"""from numpy import *
cat814test=loadtxt("814cattest.txt")
mmm=len(cat814test)
N=arange(0,mmm,1)
for i in N:
    zerz=where(cat814test[i]==0)
    q=min(min(zerz))
    qi=arange(0,q,1)
    num=min(min(zerz))
    avmag=0
    if q > 0:
        while q > 0:
            for p in qi:
                avmag=avmag+cat814test[i,p]
                q=q-1
                avgmag=avmag/num
    cat814test[i,0]=avgmag"""
