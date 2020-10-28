import subprocess
import sys,os
import glob


# Usage: python3 restart_opt.py molecule. ( You need the checkpoint file from a previous optimization!)
# E.g. If you are studying benzene and you need to restart the opt ->  python3 restart_opt.py benzene
       


def split_basis(gau_file1):        # gau_file1 is the file for the new calculation

    gau=[]
    for j in glob.glob('*.gau'):
      gau.append(j)

    f=[open(i) for i in gau]


    lines=[j.readlines() for j in f]    # lines is a list of list of strings

    n=5                                 # Skipe elements I don't need



    coord=lines[0][n:]                 # coord is a list of string


    elem=[]                             # elem are being read from your previous file
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

      f.close()





name=sys.argv[1]  






chk='%Chk=01-'+name

cwd=os.getcwd()

oldchk=[]

for i in glob.glob('*.chk'):
 oldchk.append(i)
 
oldname=os.path.join(cwd,oldchk[0])

newname=os.path.join(cwd,oldchk[0][3:])

os.rename(oldname,newname)

oldchk=os.path.splitext(os.path.basename(newname))[0]

# List containing your type of calculation


solvent=input("Choose your solvent:e.g Solvent=n,n-DiMethylFormamide:\n")


mylist=[f"%oldchk={oldchk}",chk,'%mem=16GB','%NProcShared=10',f"# pbepbe/gen pseudo=read Opt=Tight Int=UltraFine Freq Geom=Check Guess=Read empiricaldispersion=gd3bj SCRF=({solvent})",'',name,'','0 1','']

inputfile='01-'+name
print("\n")
print("%s.chk and %s are being created"%(chk,inputfile))
print("\n")
print("Read the molecular geometry from %s.chk"%(oldchk))

with open(inputfile,'w') as f:
    for i in mylist:
      f.write("%s\n" % i)


fout=open(inputfile,'a')
fout.close()

check=[s for s in mylist if 'pseudo=read' in s]

if not check:
 fout=open(inputfile,'a')
 fout.write(" \n")
 fout.close()
 print("Done")
else:
 print(" \n")
 print("Use split basis set")
 split_basis(inputfile)





process = subprocess.Popen(["sbatch","gaus.job"], stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)


