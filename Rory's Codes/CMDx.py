"""CMD.py the culmination of a summer's worth of preparation and several days straight of coding"""
from numpy import *
from pylab import *
cat =loadtxt("6819xmatchedcat.txt")
nnn=len(cat)
idx=arange(0,nnn,1)
mag606=[]
mag814=[]
x606=[]
x814=[]
x=[]
for i in idx:
    if cat[i,6] == 0:
        mag606.append(cat[i,4])
        mag814.append(cat[i,5])
    else:
        x606.append(cat[i,4])
        x814.append(cat[i,5])
        x.append(cat[i,6])
mag606=array(mag606)
mag814=array(mag814)
x606=array(x606)
x814=array(x814)
x=array(x)
diff=mag606-mag814
xdiff=x606-x814
N=len(x)
fig = figure(figsize=(5,7))
ax = fig.add_subplot(111)
for i in range (0,N):
    ax.annotate("X%d" % (x[i]), (xdiff[i],x606[i]))
scatter(diff,mag606,s=.3,c=(0.156, 0, 1))
scatter(xdiff,x606,s=40,c='red',marker='*')
axis([0, 3, 14, 25])
gca().invert_yaxis()
xlabel('Magnitude Difference(F606W-F814W)')
ylabel('Magnitude(F606W)')
savefig('6819CMDx.pdf',dpi=300)
show()
