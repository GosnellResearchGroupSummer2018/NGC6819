"""CMD.py the culmination of a summer's worth of preparation and several days straight of coding"""
from numpy import *
from pylab import *
mag606,mag814 =loadtxt("6819matchedcatalog.txt",usecols=(4,5),unpack=True)
diff=mag606-mag814
figure(figsize=(5,7))
scatter(diff,mag814,s=1)
axis([0, 3, 13, 23])
gca().invert_yaxis()
title("Color-Magnitude Diagram of Sources in NGC 6819")
xlabel('Magnitude Difference(F606W-F814W)')
ylabel('Magnitude(F814W)')
savefig('6819CMD.png')
show()
