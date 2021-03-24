from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys,operator 
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as ticker
from grab import grab_columns


# Plot homo lumo contribution  vs solvents. Oscillator strength as colormaps. It refers to the first excited state


units='eV'

gap,homo,lumo,names,lplus1,hminus1,osc,lplus2,hminus2,exc_1,h_l=grab_columns(sys.argv[1])  



osc=dict(zip(names,osc))



h_l=dict(zip(names,h_l))



 


fig=plt.figure()

ax=fig.gca()




plt.scatter(h_l.keys(), h_l.values(), marker='o',linewidths=5.5,c=list(osc.values()), cmap="viridis",vmin=0, vmax=0.5)
#plt.colorbar()
cbar=plt.colorbar()
cbar.ax.tick_params(labelsize=15)
cbar.set_label('Osc. Str. First exc',fontsize='16',fontweight='bold', labelpad=10, y=0.5)
plt.ylim(-0.05,1)
plt.xlabel('Solvent', fontsize='16',fontweight='bold')
plt.ylabel(r'H$\rightarrow$L %',fontsize='16',fontweight='bold')
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)


for label, x, y in zip(h_l.keys(),h_l.keys(), h_l.values()):
   plt.annotate(
        label,
        xy=(x, y), xytext=(-60, 60),bbox=dict(boxstyle='circle,pad=2', fc='yellow', alpha=2))

#plt.title('PbCl$_{2}$X$_{4}$',fontsize='14',fontweight='bold')
words=[sys.argv[1][0:-4],'pdf']
outfile='.'.join(words)
plt.savefig(outfile)#,bbox_inches='None',dpi=900)
plt.show()






















