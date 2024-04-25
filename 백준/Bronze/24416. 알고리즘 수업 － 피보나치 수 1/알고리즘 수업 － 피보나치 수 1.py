def fib1(n):
    if(n==1 or n==2):
        return 1
    f1=1
    f2=1
    for i in range(3,n+1):
        f3=f1+f2
        f1=f2
        f2=f3
    return f3
         

def fib2(n):
    if n==1 or n==2:
        return 1
    else:
        return n-2

N=int(input())
print(fib1(N),fib2(N))