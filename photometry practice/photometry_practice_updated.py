#This code is a basic photometry code I got as exercises originally in a Jupyter notebook designed to teach you photometry. The code is annotated with what I did and learned as I first went through this code exercise by exercise. Each exercise is separated by 8 number signs ("########"), and the first line after the separation is the title of the exercise. After completing each exercise except for the first, I added three quotes in front and after the active code for that exercise so only the one exercise I was working on ran. Just unquote a certain section of code to run it. Results can be found at <thom-ory.github.io>.

########

#Prelim Exercise: Set up code for running this program in the Mac terminal

#Code added by me after googling:
import numpy as np
from matplotlib import pylab

from IPython.core.pylabtools import *

from pylab import *
from numpy import * #Original line: '%pylab --no-import-all'   --This line originally replaced all the code above it

#from the exercises
from photutils import datasets
from astropy.visualization import LogStretch
from astropy.visualization.mpl_normalize import ImageNormalize

#After trying to run the original code n the terminal, I keep getting an error on the first line saying that the syntax is bad on the "t" in "import." It also didn't like the "%" symbol.

#I tried to run it in the Jupyter notebook gives the error "`%matplotlib` prevents importing * from pylab and numpy"

#I did some googling and found that the percent indicates a shortcut specifically for Jupyter notebooks, and replaced it with the code it's supposedly shorthand for. I also changed in which line I import matplotlib. After trying to run it in the terminal again, it now hates the "t" in import in line 6.

#Rory ws able to help me out a little and the addition of an asterisk after the t solved the syntax error. Now, running this program in the terminal gives me no error message (note: none of the code after this line was in the program when I ran it this time).

#I think I understand everything this bit of code is trying to do. I'm not exactly sure what the "*" represents, but I'd bet it's another tool like numpy or matplot lib. These few lines basically brings in everything you'd need to do basic photometry.

#After looking back at this code the next day, Marta showed me that "datasets" is not a command, but probably a practice set of data on the internet somewhere.

########

#Exercise 1: Load an image

hdu = datasets.load_star_image()
data = hdu.data[0:400, 0:400]
norm = ImageNormalize(stretch=LogStretch())

plt.imshow(data, cmap='gray_r',origin='lower',norm=norm)
"""plt.show() #added by me"""

#I can run this second bit of code (w/o the part added by me) in the Jupyter notebook on its own, and it gives the image titled "Exercise One Results" in my blog post. I can also run this code as is (with only what's written above this line, including the show command) and get the same exact image out.

#I think I'm starting to get this part of code, though I wouldn't know the syntax on my own. The first line defines a command to load the image,  the second defines where to look in the data (I'm guessing by RA and declination) and uses the first line's definition of a command to load it, and the third line defines another command about how to normalize the data. The actual computational command is the fourth line and actually creates the image, and uses the third lines command definition.

#Things I don't understand: how exactly the coordinates in the second line work, why there's a logarithmic stretch on the data to normalize and why it even needs to be normalized, why they chose the origin like they did, and where they are getting this image from. For today, I'm going to try to get as far as I can into the exercises, then in the morning I'll start trying to figure out things I didn't get the first time.

###########

#Exercise 2: Source Detection

from astropy.stats import sigma_clipped_stats
from photutils import DAOStarFinder #Original line: from photutils import daofind

mean, median, std = sigma_clipped_stats(data,sigma=3.0,iters=5)
"""print(mean, median, std)"""

#Trying to run the original code in the Jupyter notebook gives the error "ImportError: cannot import name 'Daofind'". Trying to run the code as is in the command terminal gives the exact same error. Googling revealed that the true name of the command is DAOStarFinder. After changing syntax, I get a good result. Running the program in Jupyter and the terminal give the same result, though I do have to unquote the definition of "data" and "hdu" from the last exercise for it to run in the terminal. The result is noted in the blog. Another thing to note is that running the terminal takes more time than the Jupyter notebook. The result of this exercise is recorded under Day Two on my Blog as Exercise Two Results pt. 1.

daofind = DAOStarFinder(fwhm=3.0, threshold=5*std)
sources = daofind(data - median) #Original line: 'sources = DAOStarFinder(data - median, fwhm=3.0, threshold=5.*std)'""" --replaced lines 62-63
"""log = open("/Users/computationalphysics/Desktop/githubstuff/exercise_2_pt2.txt", "w") #added by me to get the data as a text file
print(sources, file = log)""" #original line: 'print(sources)'

#Running this next bit of code in the Jupyter notebook, which a unique command line in the notebook, requires a lot of copying and pasting from previous command lines to make work. However, as long as I have the right bits of code unquoted in this text file, which I already had from the first exercises, the code works in the terminal after fixing the argument of DAOStarFinder by removing "data - median" from the argument. I'm not sure exactly how the function works with that removed or where it's pulling data from, unless it remembers from previous lines of code.

#Before I got a positive result, I kept getting the error "TypeError: __init__() got multiple values for argument 'threshold'". Googling told me that this error is often caused by not having the first argument of this type of function be 'self'. After experimenting, I tried putting "DAOStarFinder" and as the first argument of the same command and got a new error. This time it was "TypeError: __init__() got multiple values for argument 'fwhm'". I then tried removing the first argument altogether and got the result listed under Day Three, Exercise Two results pt. 2 on my blog.

#After a night of rest, I came back to the bit of code above because I knew that the result I got yesterday (Day Three on my blog) wasn't right. After a bit of googling, I ended up on <photutils.readthedocs.io> and read up on how DAOStarFinder works, and found a sample bit of code. I heard about the command daofind and couldn't figure out how to use it, but this sample code gave me the syntax. Now I get a table as the output results, listed under "Day Four Exercise 2 pt.2.1".

from photutils import CircularAperture

x = (sources['xcentroid'])
y = (sources['ycentroid'])
positions = (x,y) #Original line 'positions = (sources['xcentroid'], sources['xcentroid'])' --replaced lines 75-77
apertures = CircularAperture(positions, r=5.)
apertures.plot(color='blue', lw=1.5, alpha=0.5)
"""plt.show() #added by me"""

#Again, running this next bit of code directly from the Jupyter notebook would require a lot of copying and psting from earlier lines so the notebook note what all is being referenced, but simply keeping my old code in this text file allows me to run the program with less editing. From now on, I'm focusing on running the code through the terminal.

#Trying to run this code through the terminal gives the error "TypeError: 'DAOStarFinder' object is not subscriptable". After, googling, I'm very confused. I think I get why the error is occuring (the data given by DAOStarFinder is 2-Dimensional, and somehow the line 'positions = (sources['xcentroid'], sources['ycentroid'])' is not breaking apart the x and y data successfully), but have no idea how to fix it.

#I now think that the error is from the last part of the exercise, line 62 in the document, but after trying a couple ways of modifying the argument of DAOStarFinder, I kept getting either the same error as before or the new error.

#I was right that the error was a carryover from the last exercise and have now fixed it. I get a data table as the result of Exercise Two pt.2. Now, when trying to run the code in the terminal, I get the error "TypeError: 'function' object is not subscriptable" at line 75. Google tells me that this means Python is still reading "sources" as a function since it was last defined that way in the code, so I have to redefine it as a variable. After doing this, I get the image on my blog under "Day Four Exercise Two Results Pt.3"

########

#Excercise 3: Aperture Photometry

#This section corrects the fluxes of each star for the background flux of the sky.

#Everywhere you see "x" or "y" in the following code, it's replacing "sources['xcentroid']" and "sources['ycentroid']" in the original code from the exercises.

from photutils import CircularAnnulus
from photutils import aperture_photometry

apertures_r3 = CircularAperture(positions, r=3.)

phot_table = aperture_photometry(data, apertures_r3)
"""print(phot_table)"""

annulus_apertures = CircularAnnulus(positions, r_in=9., r_out=12.)
rawflux_r3 = aperture_photometry(data, apertures_r3)
bkgflux_table = aperture_photometry(data, annulus_apertures)

bkg_mean = bkgflux_table['aperture_sum'] / annulus_apertures.area()
"""print(bkg_mean)"""

bkg_sum = bkg_mean * apertures_r3.area()
"""print(bkg_sum)"""

final_phot_r3 = rawflux_r3['aperture_sum'] - bkg_sum
"""print(final_phot_r3)"""

#Running this code gives a series of tables, but they're all leading up to a color map, so I will only post the color map this data generates on my blog under "Day Four Exercise Three and Four Results."

########

#Exercise 4: Aperture Corrections

#This makes the flux correction more accurate by comparing the correction with a small aperture to the correction with a large aperture.

apertures_r5 = CircularAperture((x, y), r=5.) #note the larger aperture
rawflux_r5 = aperture_photometry(data, apertures_r5)

bkg_sum = bkg_mean * apertures_r5.area()
final_phot_r5 = rawflux_r5['aperture_sum'] - bkg_sum

mag_r3 = -2.5*np.log10(final_phot_r3)
mag_r5 = -2.5*np.log10(final_phot_r5)
deltamag = mag_r3 - mag_r5

plt.clf()
plt.scatter(mag_r5,deltamag)

plt.clf()
plt.scatter(mag_r5,mag_r3-mag_r5,c='k',edgecolors='none')
plt.axhline(ls='--',c='b')
plt.xlim(-15,-8)
plt.ylim(-1,1)
plt.xlabel('Mag [r=5]',fontsize=18)
plt.ylabel('$\Delta$mag',fontsize=18)

mask = [(mag_r5>-13.)&(mag_r5<-11.)&(deltamag>0.)&(deltamag<0.4)]

mean, median, std = sigma_clipped_stats(deltamag[mask], sigma=3.0, iters=5)
apcor = median
"""print(apcor)"""

plt.axhline(apcor,ls='-',c='r')
plt.show() #added by me

final_phot =-2.5*np.log10(final_phot_r3) + apcor + 25.
"""print(final_phot)"""

#Running this code as is generates a color map for the field that is refenenced in "data" in line 38, but not without errors. You can see the color map under "Exercise Three and Four Results." Before changing "sources['xcentroid']" and "sources['ycentoroid']" to "x" and "y" (given their definitions in exercise Two, I got a different, prettier color map than after I changed the names. I'll have to trouble shoot this code tomorrow, however.
