h=8
piles=[3,6,7,11]
def hrs(mid):
    x=0
    for i in piles:
        if i%mid==0:
            x+=i/mid
        else:
            x+=(i//mid)+1
    return x
start=1
end=max(piles)
while start<=end:
    print(start)
    print(end)
    mid=(start+end)//2
    if hrs(mid)>h:
        start=mid+1
    if hrs(mid)<=h:
        end=mid-1
print(start)
        
