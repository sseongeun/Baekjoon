def getGCD(A,B):
    if(A<B):
        temp=A
        A=B
        B=temp
        
    while(A%B!=0):
        rem=A%B
        A=B
        B=rem
    return B


N=int(input())
for i in range(N):
    L=list(map(int,input().split()))
    numL=L[1:]
    sum=0
    for j in range(L[0]-1):
        for k in range(j+1,L[0]):
            sum=sum+getGCD(numL[j],numL[k])
    print(sum) 
            