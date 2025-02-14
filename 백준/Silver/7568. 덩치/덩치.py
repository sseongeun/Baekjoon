
N=int(input())
data=[]
for i in range(N):
    a,b=map(int,input().split())
    data.append([i,a,b])
        
result=[]
for i in range(N):
    cnt=0
    for j in range(N):
        if data[i][1]<data[j][1] and data[i][2]<data[j][2]:
            cnt+=1
    result.append(cnt+1)
    
    
print(*result)       