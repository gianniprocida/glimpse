from matplotlib import pyplot as plt
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import sys 
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as ticker


# It takes as input the file with all calculations ( see file outputBr2.out) and gives you
# 7 lists i.e. homo, gap, hminus1,lplus1,firs_exc, lumo, oscillator strength, names


def grab_columns(abinitiofile):
    
    exc_1,gap,names,osc=[],[],[],[]
    homo,lumo,h_l=[],[],[]
    lplus1,hminus1=[],[]
    lplus2,hminus2=[],[]

    results=pd.read_csv(abinitiofile,header=None,delim_whitespace=True)
    results_sorted=results
    
    def select(DataFrame,NCols,prop):
        
        for i in range(DataFrame.shape[0]):
         prop.append(results_sorted.iloc[i,NCols])
        return prop
      
    
    
    gap=select(results_sorted,1,gap)
    
    gap.remove('HL_GAP')
   
    gap=[float(item) for item in gap]

    gap=[round(x,2) for x in gap]


    osc=select(results_sorted,9,osc)
    
    osc.remove('Osc')
   
    osc=[float(item) for item in osc]

    osc=[round(x,2) for x in osc]



    homo=select(results_sorted,2,homo)
  
    homo.remove('HOMO')

    homo=[float(item) for item in homo]

    homo=[round(x,2) for x in homo]

    
    
    hminus1=select(results_sorted,5,hminus1)
  
    hminus1.remove('HMINUS1')

    hminus1=[float(item) for item in hminus1]

    hminus1=[round(x,2) for x in hminus1]

    
    hminus2=select(results_sorted,7,hminus2)
  
    hminus2.remove('HMINUS2')

    hminus2=[float(item) for item in hminus2]

    hminus2=[round(x,2) for x in hminus2]


    lplus1=select(results_sorted,6,lplus1)
  
    lplus1.remove('LPLUS1')

    lplus1=[float(item) for item in lplus1]

    lplus1=[round(x,2) for x in lplus1]
    

    lplus2=select(results_sorted,8,lplus2)
  
    lplus2.remove('LPLUS2')

    lplus2=[float(item) for item in lplus2]

    lplus2=[round(x,2) for x in lplus2]


 

   
    lumo=select(results_sorted,3,lumo)

    lumo.remove('LUMO')
  
    lumo=[float(item) for item in lumo]

    lumo=[round(x,2) for x in lumo]


    exc_1=select(results_sorted,4,exc_1)
    exc_1.remove('First_Exc') 
    
    exc_1=[float(item) for item in exc_1]

    exc_1=[round(x,2) for x in exc_1]

    
    h_l=select(results_sorted,10,h_l)
    h_l.remove('H-L') 
    
    h_l=[float(item) for item in h_l]

    h_l=[round(x,2) for x in h_l]
   

    names=select(results_sorted,0,names)
    names.remove('species')

  
    return gap,homo,lumo,names,lplus1,hminus1,osc,lplus2,hminus2,exc_1,h_l



