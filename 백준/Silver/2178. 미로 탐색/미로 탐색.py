from collections import deque

def dfs(graph,visited,N,M):
 
    queue=deque()
    queue.append((0,0))
    visited[0][0]=True
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False and graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny]= graph[x][y]+1
                visited[nx][ny]=True
     
    return graph[N-1][M-1]
    
N,M=map(int,input().split())

graph=[]
for _ in range(N):
    graph.append(list(map(int,input())))
    
visited=[[False for _ in range(M)] for _ in range(N)]
    
print(dfs(graph,visited,N,M))
