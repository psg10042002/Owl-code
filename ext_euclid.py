a=17
b=10
t1=0
t2=1
while (a!=0 and b!=0):
    r=a%b
    q=a//b
    t=(t1-t2)*q
    a=b
    b=r
    t1=t2
    t2=t
if a==0:
    print('gcs is ',b)
else:
    print('gcd is ',a)                                                                                                                         a)
