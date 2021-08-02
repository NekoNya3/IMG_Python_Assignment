import math
d=[]

for i in range(5):
    r=input()
    k=r.split()
    d+=[k]

#print(d[0][4])
C=0
for i in range(5):
    for j in range(5):
        if d[i][j]=="1":
            C=abs(i-2)+abs(j-2)

print(C)