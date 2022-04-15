one=0
zero=0
two=0
nums=[2,0,2,1,1,0]
for i in nums:
    if i==0:
        zero+=1
    elif i==1:
        one+=1
    else:
        two+=1
nums=[0]*zero+[1]*one+[2]*two
print(nums)
