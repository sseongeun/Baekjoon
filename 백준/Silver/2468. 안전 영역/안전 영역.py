from collections import deque
import sys
input=sys.stdin.readline

N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))
        


def bfs(limit,graph,startx,starty,visited):
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    q=deque()
    q.append((startx,starty))

    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                if graph[nx][ny]>=limit:
                    q.append((nx,ny))
                    visited[nx][ny]=1
            

maxNum=0
minNum=10000
cnt=0
result=[]
for i in graph:
    if max(i)>maxNum:
        maxNum=max(i)
    if min(i)<minNum:
        minNum=min(i)
 
for f in range(minNum,maxNum+1):     
    visited=[[0]*N for _ in range(N)]
    cnt=0
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= f and not visited[i][j]:  # ✅ 방문하지 않은 영역에서 BFS 실행
                bfs(f, graph, i, j, visited)
                cnt += 1
    result.append(cnt)
            
print(max(result))
            