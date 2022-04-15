# program to print n times
def names(n,name,i):
    if n!=i:
        print(name)
        i+=1
        names(n,name,i)
    return 'end!'
    

print(names(5,'ganesh',0))
#program to find numbers from 0 to n
def printing(n,i):
    if n>=i:
        print(i)
        i+=1
        printing(n,i)
        
printing(10,1)
#program to find numbers from n to 0
def printing1(n):
    if n>0:
        print(n)
        n-=1
        printing1(n)
        
printing1(10)
#using backtracking
def back1(n):
    if n==0:
        return 0
    else:
        back1(n-1)
        print(n)
back1(10)
def sum1(n,x):
    if n<10:
        return n
    else:
        if n>0:
            n=n//10
            sum1(n,x)
            x+=n%10
        else:
            return x
        
print(sum1(1234,0))
        








    

