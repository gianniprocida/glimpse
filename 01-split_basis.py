# Read elements in your molecule

import subprocess
import sys

# Use split basis sets for different atoms
# Usage: python3 inputfile ( Inputfile should already contain all the informmation about the calculation)

# Create a set of all the atoms in your molecule

elem=[]
with open (sys.argv[1],'r') as f: 
    lines=f.readlines() 
    for line in lines: 
        if not line.rstrip():
           continue
        elif line.split()[0].isalpha():
            elem.append(line.split()[0]) 
          
                 

tot_elem=set(elem)



print("Atoms in your %s system:\n"%tot_elem)



set1=input("Put your atoms you want to treat with the 6-31g* and 0 at the end:\n")

set2=input("Put your atoms you want to treat with LANL2DZ and 0 at the end:\n")

with open (sys.argv[1],'a') as f:
   f.write("%s\n"%set1)
   f.write("6-31g*\n")
   f.write("****\n")
   f.write("%s\n"%set2)
   f.write("LANL2DZ\n")
   f.write("****\n")
   f.write(" \n")
   f.write("%s\n"%set2)
   f.write("LANL2\n")
   f.write(" \n")

process = subprocess.Popen(["sbatch","gaussian.job"], stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

