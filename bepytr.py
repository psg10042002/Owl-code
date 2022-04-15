l=[10,20,30]
n=len(l)
for i in range(2**n):
    l1=[]
    s=0
    for j in range(n):
        if i&(2**j):
            s+=l[j]
        else:
            s-=l[j]
    if s==0 or s==360:
        print(1)
        break
else:
    print(0)
