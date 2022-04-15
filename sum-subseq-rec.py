n=3
l=[1,2,1,3]
ds=[]
s=0
ind=0
n=len(l)
def subseq(ind,n,ds,l,s):
    if ind==n:
        if s==3:
            for i in ds:
                print(i,end=" ")
            print("\n")
        return 
    #to pick
    ds.append(l[ind])
    s+=l[ind]
    subseq(ind+1,n,ds,l,s)
    s-=l[ind]
    ds.pop()
    #not to pick
    subseq(ind+1,n,ds,l,s)
subseq(ind,n,ds,l,s)
