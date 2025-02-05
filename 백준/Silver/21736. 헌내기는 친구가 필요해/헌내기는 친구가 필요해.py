from collections import deque

N,M=map(int,input().split())
graph=[]
startx,starty=0,0
visited=[[0]*M for _ in range(N)]

for i in range(N):
    graph.append(list(input()))
    for j in range(M):
        if graph[i][j]=='I': # 시작점 찾기
            startx,starty=i,j
result=0

dx=[-1,1,0,0]
dy=[0,0,-1,1]  
 
q=deque()
q.append((startx,starty))
    
while q:
    x,y=q.popleft()
        
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
            
        if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0: # 아직 방문하지 않았다면
            visited[nx][ny]=1
            if graph[nx][ny]=='P':
                result+=1
                q.append((nx,ny))
            if graph[nx][ny]=='O':
                q.append((nx,ny))

if result==0:             
    print("TT")
else:
    print(result)