
import subprocess
import sys,os
import glob


# Usage: python3 state_spec.py name    , where name is the name of the molecule
       




def split_basis(gau_file1):                 #   Read the basis set the previous calculation
                                            # gau_file1 is the inputfile for the new calculation
    gau=[]
    for j in glob.glob('*.gau'):
      gau.append(j)

    f=[open(i) for i in gau]


    lines=[j.readlines() for j in f]    # lines is a list of list of strings

    n=5                                 # Skipe elements I don't need



    coord=lines[0][n:]                 # coord is a list of string


    elem=[]
    for e in coord:
     if not e.split():                  # split() method splits a string into a list
       continue
     elif e.split()[0].isalpha():
       elem.append(e.split()[0])

    [i.close() for i in f]



    tot_elem=set(elem)
    
    
    
    print("Atoms in your system %s\n"%tot_elem)
    with open (gau_file1,'a') as f:

      basis=input("Select your basis set e.g cc-pVDZ:\n")

      set1=input("Put your atoms you want to treat with %s and 0 at the end:\n" %(str(basis)))

      set2=input("Put your atoms you want to treat with LANL2DZ and 0 at the end:\n")

      f.write("%s\n"%set1)
      f.write("%s\n"%basis)
      f.write("****\n")
      f.write("%s\n"%set2)
      f.write("LANL2DZ\n")
      f.write("****\n")
      f.write(" \n")
      f.write("%s\n"%set2)
      f.write("LANL2\n")
      f.write(" \n")
      f.write("\n")
      f.close()





name=sys.argv[1]  


prefix='%chk=03-'

chk1=prefix+name

oldprefix='%oldChk=01-'
oldchk=oldprefix+name




# List containing your type of calculation

solvent=input("Select your solvent e.g DiMethylSulfoxide:\n")

mylist1=[oldchk,chk1,'%mem=16GB','%NProcShared=4',f'# cam-b3lyp/gen pseudo=read Geom=Check Guess=Read EmpiricalDispersion=GD3BJ SCRF=(Solvent={solvent},NonEquilibrium=Save)','',name,'','0 1','']

mylist2=['--Link1--',chk1,'%mem=16GB','%NProcShared=8',f'# cam-b3lyp/gen pseudo=read TD(NStates=6,Root=1) Geom=Check Guess=Read EmpiricalDispersion=GD3BJ SCRF=(Solvent={solvent},ExternalIteration,NonEquilibrium=Read)','',name,'','0 1','']


inputfile='03-'+name
print("\n")
print("%s and %s are being created"%(chk1,inputfile))
print("\n")
print("Prepare for state-specific non-eq solvation. Read non-equilibrium solvation from %s "%(oldchk))

with open(inputfile,'w') as f:
    for i in mylist1:
      f.write("%s\n" % i)


check=[s for s in mylist1 if 'pseudo=read' in s]



if not check:
 fout=open(inputfile,'a')
 fout.write(" \n")
 fout.close()
 print("Done")
else:
 print(" \n")
 print("Use split basis set")
 split_basis(inputfile)



print("\n")
print("Compute energy of the first excited state with state-specific method")
with open (inputfile,'a') as f:
    for i in mylist2:
      f.write("%s\n" %i)




check=[s for s in mylist2 if 'pseudo=read' in s]


if not check:
 fout=open(inputfile,'a')
 fout.write(" \n")
 fout.close()
 print("Done")
else:
 print(" \n")
 print("Use split basis set")
 split_basis(inputfile)


check=[s for s in mylist2 if 'SCRF=read']

if 'read' not in solvent:
  print("Done")
else:
  eps= input("Select your dielectric costant\n")
  fout=open(inputfile,'a')
  fout.write("eps=%s\n" %eps)
  fout.write("\n")
  fout.close()


command= "sed","-i",'18,$s/01/03/',"gaus.job"
subprocess.check_output(command)

command= "sed","-i",'s/opt\/freq/state-spec/',"gaus.job"
subprocess.check_output(command)



process = subprocess.Popen(["sbatch","gaus.job"], stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)


