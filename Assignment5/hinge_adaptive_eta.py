import sys
import random
import math
def dot_product(w1,d):
	dp1=0
	for j in range(0,cols,1):
		dp1= dp1 + (w1[j]*d[j])
	return dp1

###Reading Data from file
data_file=sys.argv[1]
f=open(data_file)
data=[]
line=f.readline()
while(line !=''):
	row=line.split( )
	rowf=[]
	for i in range(0,len(row),1):
		rowf.append(float(row[i]))
	rowf.append(1)
	data.append(rowf)
	line=f.readline()
num_rows=len(data)
cols=len(data[0])
f.close()
#print(data)
###Reading Labels from file
label_file=sys.argv[2]
f=open(label_file)
train_labels={}
line=f.readline()
num=[0,0]
while(line!=''):
	row=line.split( )
	train_labels[int(row[1])]=int(row[0])
	if int(row[0])==0:
		train_labels[int(row[1])]=-1	
	line=f.readline()
	num[int(row[0])]+=1
w=[]

##Initialize W
for i in range(0,cols,1):
	w.append(0.02*random.random()-0.0001)
	#print("w-test",w[i])
	

##Gradient descent 
eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001 ]
best_obj = 1000000000000000000
diff=4
k=0
error=0
for i in range(0,num_rows,1):
		if train_labels.get(i)!=None:
			dp=dot_product(w,data[i])
			check=(train_labels.get(i)*dp)
			if check<1:
				error=error + (train_labels.get(i)-(1-check))
late=error
while abs(diff)>0.001:
	dellf=[]
	for i in range(0,cols,1):
		dellf.append(0)
	diff=0
	for i in range(0,num_rows,1):
		if train_labels.get(i)!=None:
			dp=dot_product(w,data[i])
			for j in range(0,cols,1):
				check=(train_labels.get(i)*dp)
				if check<1:
					dellf[j]=dellf[j] + (data[i][j]*train_labels.get(i))
	best_eta=1
	for k in range(0, len(eta_list), 1):
		eta = eta_list[k]
		for j in range(0,cols,1):
			w[j]=w[j] +(eta*dellf[j])
		error=0
		l=0
		for i in range(0,num_rows,1):
			if train_labels.get(i)!=None:
				l=l+1
				dp=dot_product(w,data[i])
				check=(train_labels.get(i)*dp)
				if check<1:
					error=error + (1-check)
		obj=error
		if obj<best_obj:
			best_obj=obj
			best_eta=eta
		for j in range(0,cols,1):
			w[j]=w[j] -(eta*dellf[j])
	eta=best_eta
				 

####update
	for j in range(0,cols,1):
		w[j]=w[j] +(eta*dellf[j])
	error=0
	l=0
	for i in range(0,num_rows,1):
		if train_labels.get(i)!=None:
			l=l+1
			dp=dot_product(w,data[i])
			check=(train_labels.get(i)*dp)
			if check<1:
				error=error + (1-check)
	
	k=k+1
	
	#print(k,":::eta:::",eta,"::Error::",error)
	diff=error-late
	late=error
#print("W="	)
normw=0
for j in range(0,cols-1,1):
	normw=normw+(w[j]**2)
	#print(w[j])
#print("\n")
normw=normw**(1/2)
#print("||w||=",normw,"\n")

d_origin=w[len(w)-1]/normw
#print("W0=",w[len(w)-1])

####Prediction 

#print("Distance to origin=",abs(d_origin),"\n")
for i in range(0,num_rows,1):
	if train_labels.get(i)==None:
		dp=dot_product(w,data[i])
		if dp>0:
			print(1,"",i)
		else:
			print(0,"",i)


