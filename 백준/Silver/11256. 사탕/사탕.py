T=int(input())
for i in range(T):
    C,B=map(int,input().split())
    boxSize=[]
    for i in range(B):
        a,b=map(int,input().split())
        boxSize.append(a*b)
    boxSize.sort(reverse=True)
   
    sum,count=0,0
    while(sum<C):
        sum+=boxSize.pop(0)
        count+=1
    print(count)