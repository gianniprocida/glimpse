import subprocess
import sys,os
import glob


# Usage: python3 linear_resp.py name    , where name is the name of the molecule       




def split_basis(gau_file1):                 # Read the basis set from the previous calculation with named 01

    gau=[]                                 # gau_file is the inputfile for the calculation   
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

      f.close()





name=sys.argv[1]  





prefix='%chk=02-'
chk=prefix+name

oldprefix='%oldChk=01-'
oldchk=oldprefix+name


# List containing your type of calculation




mylist=[oldchk,chk,'%mem=16GB','%NProcShared=4',f"# cam-b3lyp/gen pseudo=read TD=NStates=6 Geom=Check Guess=Read empiricaldispersion=gd3bj",'',name,'','0 1','']

inputfile='02-'+name
print("\n")
print("%s and %s are being created"%(chk,inputfile))
print("\n")
print("Read the molecular geometry from %s"%(oldchk))

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



command= "sed","-i",'18,$s/01/02/',"gaus.job"
subprocess.check_output(command)

command= "sed","-i",'s/opt\/freq/td-dft/',"gaus.job"
subprocess.check_output(command)



process = subprocess.Popen(["sbatch","gaus.job"], stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)


