import imexam
from subprocess import call
import matplotlib
call(!ds9 -title frame)
imexam.list_active_ds9()
window=imexam.connect(frame)
