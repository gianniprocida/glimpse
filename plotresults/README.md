* uvvis.py -> Plot a broadened UV-vis absorption spectrum from Gaussian in nm or eV.
To run the script : python3 uvvis.py DMSO.out. (See the DMSO.pdf file as an example)


![Image](https://github.com/gianniprocida/glimpse/edit/master/plotresults/DMSO.pdf)




* total_elec.prop -> Plot of complexes vs gap, lumo, homo in one plot with multiple Y axis 
( homo and lumo are along the multiple axis). To run the script: python3 total_elec.prop.py outputPbCl2X4.out
 
 
![Image](https://github.com/gianniprocida/glimpse/edit/master/plotresults/electr_PbCl2X4.pdf)



* plt_levels.py ->  Plot homo,homo-1,homo-2, lumo, lumo+1 and lumo+2 for PbCl2X4 complexes. 
To run it: python3 plt_levels.py outputPbCl2X4.out

![Image](https://github.com/gianniprocida/glimpse/edit/master/plotresults/energylevelsPbCl2X4.pdf)


* plotHandL.py -> Plot homo and lumo levels
To run it : python3 plotHandL.py outputPbCl2X4.out

![Image](https://github.com/gianniprocida/glimpse/edit/master/plotresults/homolumoPbCl2X4.pdf)


* grab.py ->   It takes as input the file with all calculations ( see file outputBr2.out) and gives you
7 lists i.e. homo, gap, hminus1,lplus1,firs_exc, lumo, oscillator strength, names.  

* plot3Dfirstexcvssolv.py ->  Plot first excitation energy vs solvents. Oscillator strength as colormaps. 
It refers to the first excited state. To run it: python3 plot3dfirstexcvssolv.py 
