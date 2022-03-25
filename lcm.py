x=2
y=13
if y>x:
    x,y=y,x
for i in range(x,1,-1):
    if y%i==0 and x%i==0:
        lcm=i
        break
else:
    lcm=x*y
    
print(lcm)
