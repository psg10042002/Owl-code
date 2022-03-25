x=12
l=[1,2,3,6,0,1]
sum=0
count=0
for i in range(len(l)):
    sum=sum+l[i]
    if sum==x:
        print(i+1)
        break
else:
    print(0)
