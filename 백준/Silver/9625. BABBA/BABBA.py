N=int(input())

a,b=1,0
for i in range(N):
    temp=a
    a=b
    b=temp+b
    
print(a,b)
    