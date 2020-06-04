

import sys,math,random


# Input Data
datafile = sys.argv[1]
f=open("datafile")
data=[]
i=0
l=f.readline()

while(l != ''):
    a = l.split()
    dataline = []
    for i in range(0, len(a), 1):
        dataline.append(float(a[i]))
    dataline.append(1)
    data.append(dataline)
    l = f.readline()
rows = len(data)
cols = len(data[0])
f.close()

# Input labels File
labelfile = sys.argv[2]
f=open("labelfile")
ld = {}
l = f.readline()
while(l != ''):
    newlabels = l.split()
    ld[int(newlabels[1])] = int(newlabels[0])
    if(ld[int(newlabels[1])] == 0):
        ld[int(newlabels[1])] = -1
    l = f.readline()
f.close()

# Initialize W
w = []
for j in range(0, cols, 1):
    w.append(0.02 * random.random() - 0.0001)

print("Initialized W:",w)


def dot_prod_logic(v1,v2):
    result = 0
    for i in range(len(v1)):
        temp = v1[i]*v2[i]
        result += temp
    return result


et = 0.0001 # Use for Ionosphere dataset
cur = 0 
pre = 0
for k in range(0, 100000, 1):  
    delf = [0]*cols
    pre = cur
    for i in range(0, rows, 1):
        dp = dot_prod_logic(w, data[i])
        if(ld.get(i) != None):
            for j in range(0, cols, 1):
                
                delf[j] += 2*((ld[i] - dp)* data[i][j])


    for j in range(0,cols,1):
        w[j] += et*delf[j] 

    error = 0 
    for i in range(0, rows, 1):
        if(ld.get(i) != None):
            error += (ld[i] - dot_prod_logic(w, data[i]))**2
    cur = error
    if(cur > pre):
        Stp_rate = cur - pre
    else:
        Stp_rate = pre - cur
    
    if(Stp_rate < 0.001):
    #if (Stp_rate == 0.001):
        break
    print("Difference: ", Stp_rate, k)

normw = 0
for j in range(0, cols-1, 1):
    normw += w[j]**2

normw = math.sqrt(normw)
print("Norm W: ", normw)
d_origin = w[len(w)-1]/normw
print("Distance: ", abs(d_origin))



for i in range(0, rows, 1):
    if(ld.get(i) == None):
        dp = dot_prod_logic(w, data[i])
        if(dp > 0):
            print(i,"1")
        else:
            print(i,"0")
