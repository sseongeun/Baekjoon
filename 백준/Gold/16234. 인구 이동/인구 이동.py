from collections import deque
import math

country=[]
N,L,R = map(int,input().split())
for _ in range(N):
    country.append(list(map(int,input().split())))

def bfs(x,y,country,visited):
    total=0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    queue=deque([])
    queue.append([x,y])
    temp=[]
    
    while queue:
        x,y= queue.popleft()
        temp.append([x,y])
        visited[x][y]=True
        total+=country[x][y]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<N and 0<=ny<N and L<=abs(country[x][y]-country[nx][ny])<=R and visited[nx][ny]==False:
                queue.append([nx,ny])
                visited[nx][ny]=True
                
    if len(temp) >1:
        avgNum = math.floor(total/len(temp))  
        for x,y in temp:
            country[x][y]=avgNum
        return True

    return False
        

cnt=0
while True:
    visited=[[False]*N for _ in range(N)]
    move=False
    for x in range(N):
        for y in range(N):
            if visited[x][y]==False:
                if bfs(x,y,country,visited):
                    move=True
    if move==False:
        break
    cnt+=1
            
print(cnt)
            