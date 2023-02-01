import numpy as np
import os
import sys

def ReadData(fileName,C1,C2):
    FileObject=open(fileName,'r')
    DataContent=FileObject.readlines()
    RowIndex=0
    for j in DataContent:
        if j[0]!='1':
            RowIndex=RowIndex+1
            next
        else:
            break
    xdata=[]
    ydata=[]
    for j in DataContent[RowIndex+1:-2]: #chop off the initial and the last two values that are testing cycles
        x=j.split('\t')
        xdata.append(float(x[int(C1)-1]))
        ydata.append(float(x[int(C2)-1]))
    return [fileName,[np.asarray(xdata),np.asarray(ydata)]]

files=os.listdir("./")
if len(files)==1:
    print("Please move the text files you want to work on to the directory of the python script")
    sys.exit()

if len(sys.argv) <= 2:
    print('Type "Average.py x y" as you independent and dependent column data')
    sys.exit()

FilesContent=[]
for x in files:
    if x[-3:]!='TXT':
        next
    else:
        FilesContent.append(ReadData(x,sys.argv[1],sys.argv[2]))

NumFiles=len(FilesContent)
yvalues=[]
xvalues=[]
stdvalues=[]
for f in range(len(FilesContent[0][1][0])):
    dataAvg=np.zeros(NumFiles)
    for l in range(NumFiles):
        dataAvg[l]=1000*FilesContent[l][1][1][f]
    xvalues.append(FilesContent[0][1][0][f])
    yvalues.append(np.mean(dataAvg))
    stdvalues.append(np.std(dataAvg))

with open("averageData.txt","w") as ObjFileSave:
    ObjFileSave.write("#Cycles"+"\t"+"mean"+"\t"+"dev"+"\n")
    for i in range(len(xvalues)):
        ObjFileSave.write("".join(str(xvalues[i]))+"\t"+"".join(str(yvalues[i]))+"\t"+"".join(str(stdvalues[i]))+"\n")

