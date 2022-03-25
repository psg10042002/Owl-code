l=[0,1,39,76,97,123,10,34]
l=l.sort()
#using while
x=34
start=0
end=len(l)-1
while(start<=end):
    mid=(start+end)>>1
    if l[mid]==x:
        print(mid)
        break
    elif l[mid]<x:
        start=mid+1
    elif l[mid]>x:
        end=mid-1
else:
    print('not found')
    
