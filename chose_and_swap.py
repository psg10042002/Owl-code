A='ccad'
l=[i for i in A]
x=l[0]
for i in A:
    if  x!=i:
        y=i
        break
for i in range(len(l)):
    if l[i]==x:
        l[i]=y
    if l[i]==y:
        l[i]=x
l=''.join(l)
print(l)
        
