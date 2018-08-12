#make a histogram of the roundness values
from pylab import *
from scipy import *
from numpy import *
round = loadtxt('/Volumes/64FLASH/dolphotresults/ibop04/roundcol.txt')
hist(round,bins=300)

show()
