l1=[2,2,4,4,7]
l2=[2,3,4,4,7]
l=[]
def ist(x,li):
    start=0
    end=len(li)-1
    while(start<=end):
        mid=(start+end)//2
        if li[mid]==x:
            li[mid]=-1
            return x
            break
        if li[mid]<x:
            start=mid+1
        if li[mid]>x:
            end=mid-1
    return 0
    
for i in l1:
    if ist(i,l2)!=0:
        l.append(i)
    
print(l)
