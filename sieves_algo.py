#sieves algo
from math import sqrt
n=int(input())
l=[0]*2+[1]*(n-1)
for i in range(2,int(sqrt(n))+1):
    if l[i]==1:
        for j in range(i*i,n,i):
            l[j]=0
print(l.count(1))
