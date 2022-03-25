arr=[2,3,4,5,1]
def small(l,x):
        if max(l)==x:
            return 1
        else:
            return -1
            
for i in range(len(arr)):
    if i==0:
        print('-1',end=' ')
    else:
        if arr[i]>arr[i-1] and small(arr[:i],arr[i-1])==1:
            print(arr[i-1],end=' ')
        else:
            print('-1',end=' ')
