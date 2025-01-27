from collections import deque
def bfs(startX,startY,endX,endY,L,graph):
    if startX==endX and startY==endY:
        return 0
    
    dx=[1,2,2,1,-1,-2,-2,-1]
    dy=[-2,-1,1,2,-2,-1,1,2]
    
    q=deque()
    q.append((startX,startY))
    
    while q:
        x,y=q.popleft()
    
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or nx>=L or ny<0 or ny>=L:
                continue
            
            if graph[nx][ny]==0:
                q.append((nx,ny))
                graph[nx][ny]=graph[x][y]+1
    
    return graph[endX][endY]

T=int(input())
for _ in range(T):
    L=int(input()) # 한변의 길이
    graph=[[0]*L for _ in range(L)]
    startX, startY = map(int,input().split())
    endX , endY = map(int,input().split())
    print(bfs(startX,startY,endX,endY,L,graph))