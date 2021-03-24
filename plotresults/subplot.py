import sys,os
import re
import numpy as np
import matplotlib.pyplot as plt
from uvvis import search_file,broaden_spectrum
import glob
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as ticker


# Make a subplot by taking the excitations out of the *.out files. To run it: python3 subplot.py yourfilepdf

broaden,sigma,units='lorentz',0.125,'eV'

base=sys.argv[1]

f_names=[]

for j in glob.glob('*.out'):
 f_names.append(j)
if 'outputPbCl2X4.out' in f_names:
 f_names.remove('outputPbCl2X4.out')

colors=['red','blue','green','orange','brown','purple']


fig,axes=plt.subplots(6,1,sharex=True)
fig.set_facecolor('lightgrey')
for n in range(len(f_names)):
 
 osc,poles=search_file(f_names[n],units)
 axes[n].vlines(poles,[0],osc)
 Abs,Freqs=broaden_spectrum(osc,poles,broaden,sigma)
 
 name=os.path.split(f_names[n])[1][:-4]
 
 axes[n].plot(Freqs,Abs,colors[n],label=name)
 axes[n].set_xlim(5,6)
 axes[n].legend(loc='upper right')
  
 axes[n].xaxis.set_major_locator(ticker.MultipleLocator(0.1))
 axes[n].xaxis.set_minor_locator(ticker.MultipleLocator(0.05))
 


words=[base,'pdf']
outfile='.'.join(words)
plt.ylabel('Intensity',position=(0,3),fontsize='10',fontweight='bold')
plt.xlabel('Energy (eV)',fontsize='10',fontweight='bold')
plt.savefig(outfile,bbox_inches='tight',dpi=900)



plt.show()



