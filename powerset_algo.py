l=[1,2,3]
n=len(l)
for i in range(2**n):
    l1=[]
    for j in range(n):
        if i&(2**j):
            l1.append(l[j])
    print(l1)
    
            
