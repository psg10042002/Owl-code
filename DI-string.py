l="DIDI"
n=len(l)
l1=[i for i in range(n+1)]
l2=[]
for i in range(n):
    if l[i]=="I":
        l2.append(l1[0])
        l1.remove(l1[0])
    else:
        l2.append(l1[-1])
        l1.pop()
l2.append(l1[0])
print(l2)
