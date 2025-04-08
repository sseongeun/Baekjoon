from copy import deepcopy
from collections import deque

n,m = map(int,input().split()) # 세로 , 가로
graph=[]
goal=[]

for i in range(n):
    graph.append(list(map(int,input().split())))
    if 2 in graph[i]:
        goal=[i,graph[i].index(2)]

temp = deepcopy(graph)
visited=[[False for _ in range(m)] for _ in range(n)]

def dfs(temp,visited,start_x,start_y):
    temp[start_x][start_y]=0
    queue=deque()
    queue.append((start_x,start_y))
    
    visited[start_x][start_y]=True
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False and temp[nx][ny]!=0:
                queue.append((nx,ny))
                visited[nx][ny]=True
                temp[nx][ny]=temp[x][y]+1
           

dfs(temp,visited,goal[0],goal[1])

for i in range(n):
    for j in range(m):
        if temp[i][j]==1 and visited[i][j]==False:
            temp[i][j]=-1
            
for i in temp:
    print(*i)