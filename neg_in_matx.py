l=[3,2,1,-1]
start=0
end=len(l)-1
while(start<=end):
    mid=(start+end)//2
    if l[mid]<0:
        end=mid-1
    else:
        start=mid+1
print(len(l)-start)
