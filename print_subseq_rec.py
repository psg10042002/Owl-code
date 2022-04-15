n=3
l=[1,2,1]
ds=[]
ind=0
n=len(l)
def subseq(ind,n,ds,l):
    if ind==n:
        for i in ds:
            print(i,end=" ")
        print('\n')
        return 
    #to pick
    ds.append(l[ind])
    subseq(ind+1,n,ds,l)
    ds.pop()
    #not to pick
    subseq(ind+1,n,ds,l)
subseq(ind,n,ds,l)
