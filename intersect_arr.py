l1=[2,2,4,4,6,7]
l2=[1,2,2,4,4,6]
x1={}
x2={}
l=[]
for i in l1:
    if i in x1:
        x1[i]=x1[i]+1
    else:
        x1[i]=1
for i in l2:
    if i not in x2:
        x2[i]=1
    else:
        x2[i]+=1
l1=list(set(l1))
l2=list(set(l2))
for i in l1:
    if i in l2:
        if x1[i]<x2[i]:
            for j in range(x1[i]):
                l.append(i)
        else:
            for j in range(x2[i]):
                l.append(i)
print(l)
