arr=[0,1,2,2,2,4,245,69]
x=2
start=0
end=len(arr)-1
while start<=end:
    mid=int((start+end)/2)
    if arr[mid]==x:
        end=mid-1
    if arr[mid]<x:
        start=mid+1
    if arr[mid]>x:
        end=mid-1
print(start)
start=0
end=len(arr)-1
while start<=end:
    mid=int((start+end)/2)
    if arr[mid]==x:
        start=mid+1
    if arr[mid]<x:
        start=mid+1
    if arr[mid]>x:
        end=mid-1
print(end)
