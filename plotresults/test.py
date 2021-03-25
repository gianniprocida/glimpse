import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from grab import grab_columns
import sys 
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as ticker


# Plot homo,homo-1,homo-2, lumo, lumo+1 and lumo+2 for PbCl2X4 complexes. To run it: python3 plt_levels.py outputPbCl2X4.out


units='eV'

# Grab energetics from abinitiofile

gap,homo,lumo,names,lplus1,hminus1,osc,lplus2,hminus2,_,_=grab_columns(sys.argv[1])




# Plot homo

fig, ax = plt.subplots()
ax.scatter(names, homo, s=1444, marker="_",linewidth=3, zorder=3,color="blue"),#label='H')


#leg=ax.legend(markerscale=0.2)



# Plot lumo levels


ax.scatter(names, lumo, s=1444, marker="_",linewidth=3,zorder=3,color="orange")#,label='L')

#leg=ax.legend(markerscale=0.8, bbox_to_anchor=(1.1, 1.05),ncol=3, fancybox=True, shadow=True)
#ax.legend(bbox_to_anchor=(1.1, 1.05))
# Plot lumo+1 levels

ax.scatter(names, lplus1, s=1444, marker="_",linewidth=3,zorder=3,color="green")#,label='L+1')


# Plot lumo+2 levels

ax.scatter(names, lplus2, s=1444, marker="_",linewidth=3,zorder=3,color="salmon")#,label='L+2')
#leg=ax.legend(markerscale=0.8, bbox_to_anchor=(1.1, 1.05),ncol=3, fancybox=True, shadow=True)



# Plot homo-1 levels

ax.scatter(names, hminus1, s=1444, marker="_",linewidth=3,zorder=3,color="maroon",label='H-1')
#leg=ax.legend(markerscale=0.8, bbox_to_anchor=(1.1, 1.05),ncol=3, fancybox=True, shadow=True)



# Plot homo-2 levels

ax.scatter(names, hminus2, s=1444, marker="_",linewidth=3,zorder=3,color="violet")#,label='H-2')
#leg=ax.legend(markerscale=0.8, bbox_to_anchor=(0.5, 1.0),ncol=3, fancybox=True, shadow=True)



for xi,yii,yi in zip(names,lumo,homo):
    ax.annotate('', xy=(xi, yi+0.7),xycoords='data',xytext=(xi,yii-0.7),textcoords='data',
arrowprops={'arrowstyle': '<->'})
             
for xi,yii,g in zip(names,homo,gap):
   ax.annotate(f'{g} eV',xy=(xi,yi+3.7),xycoords='data',
    xytext=(5, 0), textcoords='offset points',size=10.5)




ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))

plt.title('PbCl$_{2}$X$_{4}$',fontsize='14',fontweight='bold')
plt.ylabel('Energy (%s)' % units, fontsize='14',fontweight='bold')
plt.xlabel('Solvent', fontsize='14',fontweight='bold')
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.title('PbCl$_{2}$(Sol)$_{4}$',fontsize='20',fontweight='bold')
plt.ylim(-10,2)
ax.margins(0.2)
base=sys.argv[1]
words=[base[0:-4],'levels0','pdf']
outfile='.'.join(words)
plt.savefig(outfile,bbox_inches='tight',dpi=1000)
plt.show()




