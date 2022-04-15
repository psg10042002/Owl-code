#prefix algo
a=[2,4,7,16,23,99]
l,r=map(int,input().split())
p=[0]*(len(a))
p[0]=a[0]
for i in range(1,len(a)):
    p[i]=p[i-1]+a[i]    #prefix array
if l==0:
    print(p[len(a)-1])
else:
    print(p[r]-p[l-1])
