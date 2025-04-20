from copy import deepcopy
from collections import deque

graph=[]
N,M=map(int,input().split())
for _ in range(N):
    graph.append(list(map(int,input().split())))

def bfs(graph,x,y):
    g=deepcopy(graph)
    
    queue=deque([])
    queue.append((x,y))
    
    dx=[-1,-1,0,1,1,1,0,-1]
    dy=[0,1,1,1,0,-1,-1,-1]
    visited=[[False]*M for _ in range(N)]
    visited[x][y]=True
    g[x][y]=0

    
    while queue:
        nx,ny=queue.popleft()
        
        for i in range(8):
            x,y=nx+dx[i],ny+dy[i]
            
            if 0<=x<N and 0<=y<M and g[x][y]==0 and visited[x][y]==False:
                visited[x][y]=True
                g[x][y]+=(g[nx][ny]+1)
                queue.append((x,y))
                
            if 0<=x<N and 0<=y<M and g[x][y]==1 and visited[x][y]==False:
                visited[x][y]=True
                return g[nx][ny]+1
    
          
    
result=0
for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            result=max(result,bfs(graph,i,j))
            
            
print(result)