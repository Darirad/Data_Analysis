import sys

inputFile = input('Enter the name of the topology file: ')
f = open(inputFile,'r')

letter = ['N','CA','C']

l = f.readlines()
w = []
q =[]
z = []
# row numbers where these strings are reported
for dih,j in enumerate(l):
    if '[ dihedrals ]' in j:
        w.append(dih)
    if '[ angles ]' in j:
        q.append(dih)
    if '[ cmap ]' in j:
        z.append(dih)


# generate the list of the peptide residues
topo = []
backbone = []
N  = []
CA = []
C  = []
for i in range(500): # random number, must includes the first part (all atoms) of the topology file 
    d = l[i].split()
    if '[ bonds ]' in l[i]:
        break
    if not l[i].split():
        continue
    if d[0]==';' or d[0]=='[':
        continue
    if d[0].isdigit():
        res = d[0],d[2],d[4] # atomnum, resnum, atomtype
        topo.append(res)
    if d[0].isdigit() and d[4] in letter:
        bb = d[0],d[4]
        backbone.append(bb)
for i in range(0, len(backbone)): # CMAP!!!
    if backbone[i][1] == 'C':
        C.append(backbone[i][0])
    if backbone[i][1] == 'CA':
        CA.append(backbone[i][0])
    if backbone[i][1] == 'N':
        N.append(backbone[i][0])

# generate list of the first and last residues
first = topo[0][1] #num first resid
last = topo[-1][1] #num last resid
fres = [] #first resid
lres = [] #last resid
for i in range(len(topo)):
    if topo[i][1] == first:
        fres.append(topo[i])
    if topo[i][1] ==last:
        lres.append(topo[i])

# bond
bond ='%5s %5s %12s' %(lres[-2][0],fres[0][0],'1 ;cycle')

# pairs
pair1  =  '%5s %5s %12s' %(lres[0][0],fres[0][0], '1 ;cycle')
pair2  =  '%5s %5s %12s' %(lres[2][0],fres[1][0], '1 ;cycle')
pair3  =  '%5s %5s %12s' %(lres[2][0],fres[2][0], '1 ;cycle')
pair4  =  '%5s %5s %12s' %(lres[3][0],fres[0][0], '1 ;cycle')
pair5  =  '%5s %5s %12s' %(lres[4][0],fres[0][0], '1 ;cycle')
pair6  =  '%5s %5s %12s' %(lres[-2][0],fres[3][0],'1 ;cycle')
pair7  =  '%5s %5s %12s' %(lres[-2][0],fres[4][0],'1 ;cycle')
pair8  =  '%5s %5s %12s' %(lres[-2][0],fres[-2][0],'1 ;cycle')
pair9  =  '%5s %5s %12s' %(lres[-1][0],fres[1][0],'1 ;cycle')
pair10 =  '%5s %5s %12s' %(lres[-1][0],fres[2][0],'1 ;cycle')


# angles
angle1 ='%5s %5s %5s %12s' %  (lres[2][0] ,lres[-2][0],fres[0][0],'5 ;cycle')
angle2 ='%5s %5s %5s %12s' %  (lres[-1][0],lres[-2][0],fres[0][0],'5 ;cycle')
angle3 ='%5s %5s %5s %12s' %  (lres[-2][0],fres[0][0] ,fres[1][0],'5 ;cycle')
angle4 ='%5s %5s %5s %12s' %  (lres[-2][0],fres[0][0] ,fres[2][0],'5 ;cycle')

# dihedrals
died1 ='%5s %5s %5s %5s %12s' % (lres[0][0] , lres[2][0] , lres[-2][0], fres[0][0] ,'9 ;cycle')
died2 ='%5s %5s %5s %5s %12s' % (lres[3][0] , lres[2][0] , lres[-2][0], fres[0][0] ,'9 ;cycle')
died3 ='%5s %5s %5s %5s %12s' % (lres[4][0] , lres[2][0] , lres[-2][0], fres[0][0] ,'9 ;cycle')
died4 ='%5s %5s %5s %5s %12s' % (lres[2][0] , lres[-2][0], fres[0][0] , fres[1][0] ,'9 ;cycle')
died5 ='%5s %5s %5s %5s %12s' % (lres[2][0] , lres[-2][0], fres[0][0] , fres[2][0] ,'9 ;cycle')
died6 ='%5s %5s %5s %5s %12s' % (lres[-1][0], lres[-2][0], fres[0][0] , fres[1][0] ,'9 ;cycle')
died7 ='%5s %5s %5s %5s %12s' % (lres[-1][0], lres[-2][0], fres[0][0] , fres[2][0] ,'9 ;cycle')
died8 ='%5s %5s %5s %5s %12s' % (lres[-2][0], fres[0][0] , fres[2][0] , fres[3][0] ,'9 ;cycle')
died9 ='%5s %5s %5s %5s %12s' % (lres[-2][0], fres[0][0] , fres[2][0] , fres[4][0] ,'9 ;cycle')
died10='%5s %5s %5s %5s %12s' % (lres[-2][0], fres[0][0] , fres[2][0] , fres[-2][0],'9 ;cycle')

# dihedrals
impr1 = '%5s %5s %5s %5s %12s' % (lres[-2][0],lres[2][0] ,fres[0][0],lres[-1][0],'2 ;cycle')
impr2 = '%5s %5s %5s %5s %12s' % (fres[0][0] ,lres[-2][0],fres[2][0],fres[1][0] ,'2 ;cycle')

# write the new topology file
new_inputFile = input('Enter the name of the new topology file: ')
g = open(new_inputFile,'w')

for i in range(len(l)):
    d = l[i].split()
    if not l[i].split():
        continue
    if d[0]==';' or d[0]=='[':
        g.write(l[i])
    if d[0].startswith('Protein'):
        g.write(l[i]+'\n')
    if d[0].isdigit() and d[1].isupper() :
        g.write(l[i])
    if d[0].isdigit() and d[1].isdigit():
        g.write(l[i])
    if d[0] == lres[-2][0] and d[1] == lres[-1][0] and d[2] == '1':
        g.write(bond+'\n')
        g.write(' '+'\n')
    if d[0] == lres[0][0] and d[1] == lres[-1][0] and d[2] == '1':
        g.write(pair1+'\n')
#    if d[0] == lres[2][0] and d[1] == lres[-3][0] and d[2] == '1':
        g.write(pair2+'\n')
        g.write(pair3+'\n')
    if d[0] == lres[3][0] and d[1] == lres[-1][0] and d[2] == '1':
        g.write(pair4+'\n')
    if d[0] == lres[4][0] and d[1] == lres[-1][0] and d[2] == '1':
        g.write(pair5+'\n')
    if d == l[int(q[0])-2].split():
        g.write(pair6+'\n')
        g.write(pair7+'\n')
        g.write(pair8+'\n')
        g.write(pair9+'\n')
        g.write(pair10+'\n')
        g.write(' '+'\n')
    if d[0] == lres[2][0] and d[1] == lres[-2][0] and d[2] == lres[-1][0] and d[3] =='5':
        g.write(angle1+'\n')
        g.write(angle2+'\n')
        g.write(angle3+'\n')
        g.write(angle4+'\n')
        g.write(' '+'\n')
    if d[0] == lres[0][0] and d[1] == lres[2][0] and d[2] == lres[-2][0] and d[3] ==lres[-1][0] and d[4] == '9':
        g.write(died1+'\n')
    if d[0] == lres[3][0] and d[1] == lres[2][0] and d[2] == lres[-2][0] and d[3] ==lres[-1][0] and d[4] == '9':
        g.write(died2+'\n')
    if d[0] == lres[4][0] and d[1] == lres[2][0] and d[2] == lres[-2][0] and d[3] ==lres[-1][0] and d[4] == '9':
        g.write(died3+'\n')
    if d == l[int(w[1])-2].split():
        g.write(died4+'\n')
        g.write(died5+'\n')
        g.write(died6+'\n')
        g.write(died7+'\n')
        g.write(died8+'\n')
        g.write(died9+'\n')
        g.write(died10+'\n')
        g.write(' '+'\n')
    if d == l[int(z[0])-2].split():
        g.write(impr1+'\n')
        g.write(impr2+'\n')
        g.write(' '+'\n')
    if 'cmap' in d:
        g.write(';  ai    aj    ak    al    am funct'+'\n')
        for i in range(0,len(C)):
            map =('%5s %5s %5s %5s %5s %5s \n' % (C[i-1],N[i],CA[i],C[i],N[i-(len(C)-1)],'1'))
            g.write(map)
        g.write(' '+'\n')
        g.write('; Include Position restraint file'+'\n')
        g.write('#ifdef POSRES'+'\n')
        if l[len(l)-3].startswith('#include'):
            g.write(l[len(l)-3])
        g.write('#endif'+'\n')
        break
g.close()


