#This code is a basic photometry code I got as exercises originally in a Jupyter notebook designed to teach you photometry. The code is annotated with what I did and learned as I first went through this code exercise by exercise. Each exercise is separated by 8 number signs ("########"), and the first line after the separation is the title of the exercise. After completing each exercise except for the first, I added three quotes in front and after the active code for that exercise so only the one exercise I was working on ran. Just unquote a certain section of code to run it.

########

#Exercise: Set up code for running this program in the Mac terminal

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

#Exercise: Load an image

hdu = datasets.load_star_image()
data = hdu.data[0:400, 0:400]
norm = ImageNormalize(stretch=LogStretch())

plt.imshow(data, cmap='Greys',origin='lower',norm=norm)
plt.show() #added by me

#I can run this second bit of code (w/o the part added by me) in the Jupyter notebook on its own, and it gives the image titled "Exercise One Results" in my blog post. I can also run this code as is (with only what's written above this line, including the show command) and get the same exact image out.

#I think I'm starting to get this part of code, though I wouldn't know the syntax on my own. The first line defines a command to load the image,  the second defines where to look in the data (I'm guessing by RA and declination) and uses the first line's definition of a command to load it, and the third line defines another command about how to normalize the data. The actual computational command is the fourth line and actually creates the image, and uses the third lines command definition.

#Things I don't understand: how exactly the coordinates in the second line work, why there's a logarithmic stretch on the data to normalize and why it even needs to be normalized, why they chose the origin like they did, and where they are getting this image from. For today, I'm going to try to get as far as I can into the exercises, then in the morning I'll start trying to figure out things I didn't get the first time.

###########

#Exercise: Source Detection

"""from astropy.stats import sigma_clipped_stats
from photutils import DAOStarFinder
#Original line: from photutils import daofind

mean, median, std = sigma_clipped_stats(data,sigma=3.0,iters=5)
print(mean, median, std)"""

#Trying to run the original code in the Jupyter notebook gives the error "ImportError: cannot import name 'Daofind'," which I think is because it's defined in a different command line in the Jupyter notebook. Trying to run the code as is in the command terminal gives the exact same error. Googling revealed that the true name of the command is DAOStarFinder. Running the program in Jupyter and the terminal give the same result, though I do have to unquote the definition of "data" and "hdu" from the last exercise. The result is noted in the blog. Another thing to note is that running the terminal takes more time than the Jupyter notebook. The result of this exercise is recorded under Day Two on my Blog as
