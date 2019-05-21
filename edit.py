import csv 

input = open('data.csv', 'r',encoding="utf8", errors='ignore')
output = open('out.csv', 'w')
writer = csv.writer(output)
for row in csv.reader(input):
    if row:
        if ',' in row[0]:
            row[0]=row[0].replace(',', '.')
        if ',' in row[12]:
            row[12]=row[12].replace(',', '.')
        writer.writerow(row)
        
from more_itertools import unique_everseen
with open('out.csv','r') as f, open('data2.csv','w') as out_file:
    out_file.writelines(unique_everseen(f))
input.close()
output.close()








