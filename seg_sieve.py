def prime(L, R):
    from math import sqrt
    l=[]
    l1=[]
    def sieve(n):
        a=[1]*n
        a[0],a[1]=0,0
        for i in range(2,int(sqrt(n))+1):
            if a[i]==1:
                for j in range(i*i,n,i):
                    a[j]=0
        return a
    primes=sieve(int(sqrt(R))+1)
    print(primes)
    dummy=[1]*(R-L+1)
    if L==0:
        dummy[0]=0
    if L==1:
        dummy[1]=0
        dummy[0]=0
    for i in range(2,len(primes)):
        if primes[i]==1:
            l.append(i)
    print(l)
    for i in l:
        fm=(L//i)*i
        if(fm<L):
            fm=fm+i
        fm=max(fm,i*i)
        print(fm)
        for j in range(fm,R+1,i):
            dummy[j-L]=0
    for i in range(len(dummy)):
        if dummy[i]==1:
            l1.append(L+i)
    return l1
L=int(input())
R=int(input())
print(prime(L,R))
