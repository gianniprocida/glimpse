import pandas as pd
import docx
c=8065.73 
osc,energy=[],[] 
i,j=[],[]
contr=[] 
k,e,g,y=[],[],[],[]
exc=['E$1$','E$2$','E$3$','E$4$','E$5$','E$6$','E$7$','E$8$','E$9$','E$10$']
searchfile=open('UVData.txt','r') 
for line in searchfile: 
        if 'HOMO' in line: 
            next(searchfile) 
            for line in searchfile: 
                osc.append(line.split()[3]) 
                i.append(line.split()[5]) 
                j.append(line.split()[6])
                k.append(line.split()[7])
                e.append(line.split()[8])
                g.append(line.split()[9])
                y.append(line.split()[10])
                energy.append(float(line.split()[1])/c)
                 
first=[a+b for a,b in zip(i,j)]
second=[a+b for a,b in zip(k,e)]
third=[a+b for a,b in zip(g,y)]
comp=[a+b for a,b in zip(first,second)]

energy=[round(float(item),2) for item in energy]

osc=[round(float(item),2) for item in osc]


df=pd.DataFrame(dict(Excitation=exc, Energy=energy,OS=osc,Composition=comp))



print(df.to_latex(index=True))


