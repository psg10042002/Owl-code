l=[2,3,7,10,11]
r=int(input())
for i in range(r):
    s,e,x=map(int,input().split())
    for j in range(s,e):
        l[j]+=x
print(l)
