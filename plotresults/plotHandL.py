import numpy as np
import matplotlib.pyplot as plt
from grab import grab_columns
import sys 
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as ticker


# Plot homo and lumo levels


units='eV'

# Grab energetics from abinitiofile

gap,homo,lumo,names,lplus1,hminus1,osc,lplus2,hminus2,_,_=grab_columns(sys.argv[1])




# Plot lumo

orbitals = ["$LUMO$", "$LUMO$","$LUMO$","$LUMO$", "$LUMO$","$LUMO$"]
fig, ax = plt.subplots()
ax.scatter(names, homo, s=1444, marker="_",linewidth=3, zorder=3,color="blue")
ax.grid(axis='y')

for xi,yi,tx in zip(names,lumo,orbitals):
    ax.annotate(tx, xy=(xi,yi), xytext=(0,-4), size=11,
                ha="center", va="top", textcoords="offset points")




# Plot homo levels


orbitals = ["$HOMO$", "$HOMO$","$HOMO$","$HOMO$", "$HOMO$","$HOMO$"]
ax.scatter(names, lumo, s=1444, marker="_",linewidth=3,zorder=3,color="orange")

ax.grid(axis='y')


for xi,yi,tx in zip(names,homo,orbitals):
    ax.annotate(tx, xy=(xi,yi), xytext=(0,-4), size=11,
                ha="center", va="top", textcoords="offset points")

# Plot lumo levels

for xi,yii,yi in zip(names,lumo,homo):
    ax.annotate('', xy=(xi, yi+0.7),xycoords='data',xytext=(xi,yii-0.7),textcoords='data',
arrowprops={'arrowstyle': '<->'})
             
for xi,yii,g in zip(names,homo,gap):
   ax.annotate(f'{g} eV',xy=(xi,yi+3.7),xycoords='data',
    xytext=(5, 0), textcoords='offset points')

ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))

plt.title('PbCl$_{2}$X$_{4}$',fontsize='16',fontweight='bold')
plt.ylabel('Energy (%s)' % units, fontsize='14',fontweight='bold')
plt.xlabel('Solvent', fontsize='14',fontweight='bold')
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.ylim(-10,2)
ax.margins(0.2)
base=sys.argv[1]
words=[base[0:-4],'levels','pdf']
outfile='.'.join(words)
plt.savefig(outfile,bbox_inches='tight',dpi=900)
plt.show()






