import subprocess
import sys,os


# Usage: python3 opt_freq.py gau_file. (e.g. python3 opt_freq.py benzene.gau)
# The script creates the input file for a optimization in gaussian ( modify the list if you need something else) 

# split_basis() function write the basis set into the new calculation (gau_file1)

def split_basis(gau_file0,gau_file1):        # gau_file1 is the file for the new calculation           
    fout=open(gau_file1,'a')                #  gau_file0 is the file file the initial geometetry ( the input you give to the script)
    elem=[]                                 
    with open (gau_file0,'r') as f:          # Read elements from gau_file0      
        lines=f.readlines()
        for line in lines:
            if not line.rstrip():   # Leave out blank lines
               continue
            elif line.split()[0].isalpha():
                elem.append(line.split()[0])


    tot_elem=set(elem)



    print("Atoms in your system %s\n"%tot_elem)

    basis=input("Select your basis set e.g cc-pVDZ:\n")

    set1=input("Put your atoms you want to treat with %s and 0 at the end:\n" %(str(basis)))

    set2=input("Put your atoms you want to treat with LANL2DZ and 0 at the end:\n")

    fout.write("%s\n"%set1)
    fout.write("%s\n"%basis)
    fout.write("****\n")
    fout.write("%s\n"%set2)
    fout.write("LANL2DZ\n")
    fout.write("****\n")
    fout.write(" \n")
    fout.write("%s\n"%set2)
    fout.write("LANL2\n")
    fout.write(" \n")

    fout.close()


       
molecule=os.path.splitext(sys.argv[1])[0]


fin=open("gaussian.job","r")
fout=open("gaus.job","w")

for line in fin:
 fout.write(line.replace('PbI2_acn',molecule))

fin.close()
fout.close()

prefix='%Chk=01-'
chkname=prefix+molecule

# List containing your type of calculation. You have to write the whole equality otherwise you can't use SCRF=(read)!

solvent=input("Choose your solvent:e.g Solvent=n,n-DiMethylFormamide:\n")


mylist=[chkname,'%mem=16GB','%NProcShared=8',f"# cam-b3lyp/Gen pseudo=read Opt Freq EmpiricalDispersion=GD3BJ SCRF=({solvent})"]


inputfile='01-'+molecule
print("%s and %s are being created"%(chkname,inputfile))
print(" \n")
with open(inputfile,'w') as f:
    for i in mylist:
      f.write("%s\n" % i)

fin=open(sys.argv[1],'r')
coordinates=fin.read()
fin.close()


fout=open(inputfile,'a')
fout.write(coordinates)
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
 
 split_basis(sys.argv[1],inputfile)


check=[s for s in mylist if 'SCRF=read']

if 'read' not in solvent:
  print("Done")
else:
  eps= input("Select your dielectric costant\n")
  fout=open(inputfile,'a')
  fout.write("eps=%s\n" %eps)
  fout.write("\n")
  fout.close()

command= "sed","-i","-e",'/Put/d',inputfile
subprocess.check_output(command) #  Run command with arguments and return its output as a byte string.

cwd=os.getcwd()
os.chmod(os.path.join(cwd,'gaus.job'),0o777)
process = subprocess.Popen(["sbatch","gaus.job"], stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
