height = [1,8,6,2,5,4,8,3,7]
c=0
for i in range(len(height)):
    for j in range(i+1,len(height)):
        x=min(height[i],height[j])
        x=x*(j-i)
        if x>c:
            c=x
print(c)
