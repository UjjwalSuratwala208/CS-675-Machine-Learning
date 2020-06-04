# import libraries
import math
import sys

datafile = sys.argv[1]
f=open(datafile)

data=[]
l=f.readline()
while (l != ''):
    a=l.split()
    l2=[]
    for j in range(0, len(a), 1):
        l2.append(int(a[j]))
    data.append(l2)
    l=f.readline()
rows=len(data)
cols =len(data[0])
f.close()

labelfile = sys.argv[2]
f=open(labelfile)

trainlabels= []
l=f.readline()
while(l != ''):
    a=l.split()
    trainlabels.append(int(a[0]))
    l=f.readline()
f.close()


testfile = sys.argv[3]
f=open(testfile)


testdata=[]

l=f.readline()
while (l != ''):
    a=l.split()
    l2=[]
    for j in range(0, len(a), 1):
        l2.append(int(a[j]))
    testdata.append(l2)
    l=f.readline()
f.close()

def feature_selection(data, trainlabels):
    chisqlist = []
    for j in range(0, len(data[0]),1):
	    observed = [[1,1],[1,1],[1,1]]    
	    for i in range(0, len(data),1):
	        if trainlabels[i] == 0:
	            if data[i][j] == 0:
	                observed[0][0] += 1
	            elif data[i][j] == 1:
	                observed[1][0] += 1
	            elif data[i][j] == 2:
	                observed[2][0] += 1
	        elif trainlabels[i] == 1:
	            if data[i][j] == 0:
	                observed[0][1] += 1
	            elif data[i][j] == 1:
	                observed[1][1] += 1
	            elif data[i][j] == 2:
	                observed[2][1] += 1
	    
	    colss = [ sum(x) for x in observed]
	   
	    rowss = [ sum(x) for x in zip(*observed) ]
	    
	    total = sum(colss)
	    
	    expected = [[(row*col)/total for row in rowss] for col in colss]
	    
	    chisq = [[((observed[i][j] - expected[i][j])**2)/expected[i][j] for j in range(0,len(expected[0]),1)] for i in range(0,len(expected),1)]
	    
	    final_chisq = sum([sum(x) for x in zip(*chisq)])
	    
	    chisqlist.append(final_chisq)
    
    chi_sort = sorted(range(len(chisqlist)), key=chisqlist.__getitem__, reverse=True)
    index = chi_sort[:15]
    return index


def reduced_data(data, column_no):
	red_data = []
	l1 = list(zip(*data))
	for j in column_no:
		red_data.append(l1[j])
	red_data = list(zip(*red_data))
	return red_data
	
column_no = feature_selection(data, trainlabels)
print(column_no)
feature_file=open("feature.txt",mode="w",encoding="utf-8")

for i in range(0, len(column_no),1):
    st=str(column_no[i])
    feature_file.write(st + "\n")

red_data=reduced_data(data, column_no)
red_testdata=reduced_data(testdata, column_no)

from sklearn import svm
clf = svm.SVC(kernel='rbf', C = 1.0, gamma=0.001)
clf.fit(red_data,trainlabels)
pred_list=clf.predict(red_testdata)
pred_file=open("predicted_labels.txt",mode="w",encoding="utf-8")

for i in range(0, len(pred_list),1):
    st=str(i)+" "+str(pred_list[i])
    pred_file.write(st + "\n")
    

