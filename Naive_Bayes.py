

import  sys

datafile = sys.argv[1]
f = open(datafile, 'r')

data=[]
i=0
l=f.readline()

#############
##Read data
############

while(l!=''):
	a=l.split()
	l2=[]
	for j in range(0,len(a),1):
		l2.append(float(a[j]))
	data.append(l2)
	l=f.readline()
rows=len(data)
cols=len(data[0])
f.close()


labelfile = sys.argv[2]

f = open(labelfile)


trainlabels={}
n=[]
n.append(0)
n.append(0)
l=f.readline()
while(l !=''):
	a=l.split()
	trainlabels[int(a[1])]=int(a[0])
	l =f.readline()
	n[int(a[0])]+=1
m0=[]
for j in range(0,cols,1):
	m0.append(1)
m1=[]
for j in range(0,cols,1):
	m1.append(1)
for i in range(0,rows,1):
	if(trainlabels.get(i)!=None and  trainlabels[i]==0):
		for j in range(0,cols,1):
			m0[j]=m0[j]+data[i][j]
	if(trainlabels.get(i)!=None and trainlabels[i]==1):		
		for j in range(0,cols,1):
			m1[j]=m1[j]+data[i][j]

for j in range(0,cols,1):
	m0[j]=m0[j]/n[0]
	m1[j]=m1[j]/n[1]




sd0=[]
sd0.append(0)
sd1=[]
sd1.append(0)

sqsd0=[]
for j in range(0,cols,1):
        sqsd0.append(0)
sqsd1=[]
for j in range(0,cols,1):
        sqsd1.append(0)
for i in range(0,rows,1):
        if(trainlabels.get(i)!=None and  trainlabels[i]==0):
                for j in range(0,cols,1):
                        sqsd0[j]=(m0[j]-data[i][j])**2
        if(trainlabels.get(i)!=None and trainlabels[i]==1):
                for j in range(0,cols,1):
                        sqsd1[j]=(m1[j]-data[i][j])**2
                        
for j in range(0,cols,1):
        sd0.append(0)
        sd1.append(1)
        sd0[j]=(sqsd0[j]/n[0])**0.5
        sd1[j]=(sqsd1[j]/n[1])**0.5


ad=[]
for j in range(0,cols,1):
        ad.append(0)
s=[]
for j in range(0,cols,1):
        s.append(0)
for i in range(0,rows,1):
        if(trainlabels.get(i)==None):
                ad=0
                s=0
                for j in range(0,cols,1):
                        ad=((m0[j]-data[i][j])/sd0[j])**2
                        s=((m1[j]-data[i][j])/sd1[j])**2
                if(ad<s):
                        print("0",i)
                else:
                        print("1",i)
