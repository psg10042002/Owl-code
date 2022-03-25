def fib(n,last):
    x=[]
    a=0
    b=1
    if n==1:
        print(a)
        
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            if last>=b or last>=a:
                x.append(a)
               
            print(c)
    print('maximum value before entered value is',max(x))
        

x=int(input('enter no of fabinocci :'))
y=int(input('enter a value:'))
fib(x,y)
            

