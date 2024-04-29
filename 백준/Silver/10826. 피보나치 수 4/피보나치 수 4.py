n=int(input())
f0=0;f1=1;f3=0
if n==0:
    print(f0)
elif n==1:
    print(f1)
else:
    for i in range(n-1):
        f3=f0+f1
        f0=f1
        f1=f3
    print(f3)   