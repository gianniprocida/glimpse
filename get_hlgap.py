import os,fnmatch,sys
import pandas as pd



def skip_lines(f,num):    # f is the file object 
 for i in range(num):
   next(f)


def find_files(dir_look):
    total=[]
   
    for subdirs,dirnames,files in os.walk(dir_look):
      for f in fnmatch.filter(files,'*02-*'):       # Find files with *02-*
        total.append(os.path.join(subdirs,f))
        matches=[f for f in total if '.out' in f]   # Find files which ends with .out
        dirs=[os.path.basename(os.path.dirname(f)) for f in matches]   # Extracts directory
    return matches,dirs


cwd=os.getcwd()


_,names=find_files(cwd)

matches,_=find_files(cwd)

homo=[]
lumo=[]



files=[open(i,'r') for i in matches]


conversionfactor=21.211396   # a.u. to eV

for i in files:
    for line in i: 
        rules=[ 'Alpha  occ. eigenvalues' in line, len(line.split())!=9]  # Check if all items are true
        if all(rules):
          homo.append(float(line.split()[-1])*conversionfactor)
          break

    line=next(i)
    lumo.append(float(line.split()[4])*conversionfactor)

[i.close() for i in files]       


gap=[]
for i in range(len(homo)):
 gap.append(lumo[i]-homo[i])#*conversionfactor


df=pd.DataFrame(dict(species=names,HL_GAP=gap,HOMO=homo,LUMO=lumo))
with open('output.out','w') as f:
 df.to_string(f,index=False)


# Why break is necessary?
#When the end of an iterator is reached, program searches for the default value. 
#If a default value is not given for such cases, then it will raise StopIteration error.
# Break avoid the end of an iterator .



