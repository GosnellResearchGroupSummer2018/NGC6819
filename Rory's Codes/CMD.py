"""CMD.py the culmination of a summer's worth of preparation and several days straight of coding"""
from numpy import *
from pylab import *
mag606,mag814 =loadtxt("6819matchedcatalog.txt",usecols=(4,5),unpack=True)
diff=mag606-mag814
figure(figsize=(5,7))
scatter(diff,mag606,s=.3,c=(0.156, 0, 1))
axis([0, 3, 14, 25])
gca().invert_yaxis()
xlabel('Magnitude Difference(F606W-F814W)')
ylabel('Magnitude(F606W)')
savefig('6819CMD.pdf',dpi=300)
show()
