def sum1(n,s):
    if n==0:
        print(s)
    else:
        s+=n%10
        sum1(n//10,s)

sum1(1022,0)
def sum1(n):
    if n==0:
        return 0
    return n%10+sum1(n//10)
print(sum1(1097))
def count(n,i):
    if n==0:
        return i
    i+=1
    return count(n//10,i)
print(count(1002435,0))
def count1(n):
    if n==0:
        return 0
    return 1+count1(n//10)
print(count1(6456))
