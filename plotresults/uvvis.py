import sys
import re,os
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.ticker as ticker









def search_file(f_name,units):
    ''' Grabs all the oscillator strengths and excitation energies '''

    # grab poles/oscillator strengths
    osc, poles = [], []
    searchfile = open(f_name, "r")
    for line in searchfile:
        if 'Excited State' in line:
            contents = re.split('\s+|=',line)
            osc.append(float(contents[10]))
            if units == 'eV':
                poles.append(float(contents[5]))
            elif units == 'nm': 
                poles.append(float(contents[7]))
            else:
                print('Units: %s not available' % units)
                sys.exit()
    searchfile.close()

    return osc, poles

def broaden_spectrum(osc,poles,b_type,sigma):
    ''' Broaden poles to have a particular line shape '''

    npnts = 3000

    # define the range of frequencies
    pole_min, pole_max = min(poles)-4, max(poles)+4
    freq_step = (pole_max - pole_min) / npnts
    freq = [pole_min + i*freq_step for i in range(npnts)]
#   print('Broadening Scheme selected:%s'%b_type)

    # Build absorption spectrum by brodening each pole
    Abs = np.zeros([npnts])
    for i in range(len(osc)):
        for j in range(npnts):
            if b_type == 'lorentz':
                x       = (poles[i] - freq[j]) / (sigma/2)
                Abs[j] += osc[i] / (1 + x**2)
            
            elif b_type=='gaussian':
                x       = (poles[i] - freq[j]) / (sigma/2)
                Abs[j] += osc[i]*np.exp(-(np.log(2))*x**2)
                
            else:
                sys.exit()
            
    return Abs, freq

def plot_spectrum(Abs,freq,osc,poles,title,units):

    fig = plt.figure()  
    ax  = fig.gca()
    ax.plot(freq,Abs,'brown',linewidth=3.5)
    ax.vlines(poles,[0],osc,linestyle='dashed')
    plt.xlim(5,6.95)
   
    plt.xlabel('Energy (%s)' % units)
    plt.ylabel('Intensity ')
    plt.xlabel('Energy (%s)' % units, fontsize='10',fontweight='bold')
    plt.ylabel('Intensity ',fontsize='10',fontweight='bold')
   
   
    ax.text(0.0, 0.1,'', fontsize=14,transform=ax.transAxes)
    ax.tick_params(which='major', width=1.00)
    ax.tick_params(which='major', length=5)
    ax.tick_params(which='minor', width=0.75)
    ax.tick_params(which='minor', length=2.5)
    ax.xaxis.set_ticks_position('bottom')

if __name__ == '__main__':
 

    sigma, units,broaden = 0.125, 'eV','lorentz'
    osc,poles=search_file(sys.argv[1],units)
    base=  os.path.splitext(sys.argv[1])
    Abs, freqs = broaden_spectrum(osc,poles,broaden,sigma)

   
    # shift spectrum and plot
    shift   = 0 # eV
    freqs   = [freq+shift for freq in freqs] 
    poles   = [pole+shift for pole in poles] 
    plot_spectrum(Abs,freqs,osc,poles,title,units)
    
    words=[base[0],'pdf']
    outfile='.'.join(words)
    plt.savefig(outfile,bbox_inches='tight',dpi=900)
    plt.show()
