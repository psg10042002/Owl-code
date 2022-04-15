beans = [2,10,3,2]
beans.sort()
print(beans)
p=[1]*len(beans)
p[0]=beans[0]
for i in range(1,len(p)):
    p[i]=p[i-1]+beans[i]
print(p)
c=0

n=len(p)
c1=p[-1]
for i in range(len(p)):
    c=p[-1]-(n*beans[i])
    print(c)
    n-=1
    if c1>c:
        c1=c
print(c1)   
        
