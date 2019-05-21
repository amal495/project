import csv
import numpy as np 
def to_array(l,name) :
    n=np.array(l)
    p=0
    m=np.zeros(shape=(80,80,80))
    for i in range(80):
        for j in range(80):
            for k in range(80):
                m[i][j][k]=n[p]
                p=p+1
    np.save(name,m)
  
     
input = open('data2.csv', 'r',encoding="utf8", errors='ignore')
output = open('set2.csv', 'w')
writer = csv.writer(output)
i=0
reader=csv.reader(input)
head=next(reader)
head=head[:13]
head.append('voxels.npy')
writer.writerow(head)
for row in reader:
        name='set'+str(i)
        l=row[13:]
        to_array(l,name)
        row=row[:13]
        row.append(name)
        writer.writerow(row)
        i=i+1

def to_array(l,name) :
    n=np.array(l)
    p=0
    m=np.zeros(shape=(80,80,80))
    for i in range(80):
        for j in range(80):
            for k in range(80):
                m[i][j][k]=n[p]
                p=p+1
    np.save(name,m)
  
        
input.close()
output.close()
