import matplotlib.pyplot as plt
from grab import grab_columns
import sys
from matplotlib.font_manager import FontProperties

# 3D-Plot of complexes vs gap, lumo, homo in one plot. To run the script: python3 total_elec.prop.py outputPbCl2X4.out


gap,homo,lumo,names,lplus1,hminus1,osc,lplus2,hminus2,_,_=grab_columns(sys.argv[1])






def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)


fig, host = plt.subplots()
fig.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()

# Offset the right spine of par2.  The ticks and label have already been
# placed on the right by twinx above.
par2.spines["right"].set_position(("axes", 1.25))
# Having been created by twinx, par2 has its frame off, so the line of its
# detached spine is invisible.  First, activate the frame but make the patch
# and spines invisible.
make_patch_spines_invisible(par2)
# Second, show the right spine.
par2.spines["right"].set_visible(True)




p1, = host.plot(names,gap, "o-", label="Band gap",color='black')
p2, = par1.plot(names,homo, "r->", label="HOMO",color='blue')
p3, = par2.plot(names,lumo, "ks-", label="LUMO",color='orange')

#host.set_xlim(0, 2)
host.set_ylim(7.20,10.5)


par1.set_ylim(-6.7, -10)
par2.set_ylim(-0.1, 1.2)

#host.set_xlabel("Distance")
host.set_ylabel("Band gap (eV)",fontsize='16',fontweight='bold')
par1.set_ylabel("HOMO level (eV)",fontsize='16',fontweight='bold')
par2.set_ylabel("LUMO level (eV)",fontsize='16',fontweight='bold')

host.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())
par2.yaxis.label.set_color(p3.get_color())

tkw = dict(size=4, width=1.5)
host.tick_params(axis='y', colors=p1.get_color(), **tkw,labelsize=15)
par1.tick_params(axis='y', colors=p2.get_color(), **tkw,labelsize=15)
par2.tick_params(axis='y', colors=p3.get_color(), **tkw,labelsize=15)
host.tick_params(axis='x', **tkw,labelsize=15)

lines = [p1, p2, p3]

host.legend(lines, [l.get_label() for l in lines])
#plt.title('PbI$_{2}$X$_{4}$',fontsize='14',fontweight='bold')
base=sys.argv[1]
words=[base[0:-4],'pdf']
outfile='.'.join(words)
plt.savefig(outfile,bbox_inches='tight',dpi=900)
plt.show()
plt.show()
