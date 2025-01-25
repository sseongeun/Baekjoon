import heapq
M,N=map(int,input().split())
graph=[]
INF=int(1e9)
dist=[[INF]* M for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int,input())))
    

    
def bfs(x,y,start):
    
    q=[]
    heapq.heappush(q,(x,y,start))
    dist[x][y]=0
    
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]

    
    while q:
        
        num,x,y=heapq.heappop(q)
        
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            
            if 0<=nx<N and 0<=ny<M:
                new_num= num+graph[nx][ny]
                
                if new_num< dist[nx][ny]:
                    heapq.heappush(q,(new_num,nx,ny))
                    dist[nx][ny]=new_num
    return dist[N-1][M-1]
    

    
print(bfs(0,0,0))