from collections import deque

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
        
def dfs(x,y):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    q=deque()
    q.append((x,y))
    graph[x][y]=0
    count=1
    
    while q:
        x,y=q.popleft()
    
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                graph[nx][ny]=0
                q.append((nx,ny))
                count+=1
    return count

       

result=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            result.append(dfs(i,j))
            
            
print(len(result))
if len(result)==0:
    print("0")
else:
    print(max(result))