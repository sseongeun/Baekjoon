array=[[0]*101 for _ in range(101)]
N=int(input())
for i in range(N):
    a,b=map(int,input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            array[i][j]=1
  
result=0          
for i in range(101):
    for j in range(101):
        if array[i][j]==1:
            result+=1

print(result)