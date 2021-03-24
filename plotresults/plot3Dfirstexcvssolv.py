from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys,operator 
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as ticker
from grab import grab_columns


units='eV'

# Plot first excit energy vs solvents. Oscillator strength as colormaps. It refers to the first excited state


# Grab energetics from abinitiofile
       
gap,homo,lumo,names,lplus1,hminus1,osc,lplus2,hminus2,exc_1,h_l=grab_columns(sys.argv[1])  


# Create two dictionaries using names and exc_1 lists

exc=dict(zip(names,exc_1))
osc=dict(zip(names,osc))



h_l=dict(zip(names,h_l))




fig=plt.figure()

ax=fig.gca()


# Plot first excitation energy vs solvents. Oscillator strength as colormaps


plt.scatter(h_l.keys(), exc.values(), marker='o',linewidths=5.5,c=list(osc.values()), cmap="viridis",vmin=0, vmax=0.5)

cbar=plt.colorbar()
cbar.ax.tick_params(labelsize=15)
cbar.set_label('Osc. Str.',fontsize='16',fontweight='bold', labelpad=10, y=0.5)

plt.xlabel('Solvent', fontsize='16',fontweight='bold')
plt.ylabel('First exc (eV)',fontsize='16',fontweight='bold')
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.2))
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
plt.ylim(5.2,6.6)


for label, x, y in zip(h_l.keys(),h_l.keys(), h_l.values()):
   plt.annotate(
        label,
        xy=(x, y), xytext=(-60, 60),bbox=dict(boxstyle='circle,pad=2', fc='yellow', alpha=2))

#plt.title('PbCl$_{2}$X$_{4}$',fontsize='14',fontweight='bold')
words=[sys.argv[1][0:-4],'pdf']
outfile='.'.join(words)
plt.savefig(outfile)#,bbox_inches='None',dpi=900)
plt.show()






















