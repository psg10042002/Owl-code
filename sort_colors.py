nums=[0,0]
start=0
end=len(nums)-1
mid=(start+end)//2
while(mid<=end):
    if nums[mid]==0:
        nums[mid],nums[start]=nums[start],nums[mid]
        start+=1
        mid=(start+end)//2
    elif nums[mid]==2:
        nums[mid],nums[end]=nums[end],nums[mid]
        end-=1
        mid=(start+end)//2
    else:
        mid+=1   
print(nums)        
