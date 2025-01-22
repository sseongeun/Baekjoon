import heapq
INF=int(1e9)
count=1


def dijackstra(graph):
    global count
    count+=1
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    distance=[[INF] *N for _ in range(N)]
    
    q=[]
    heapq.heappush(q,(graph[0][0],0,0))
    distance[0][0]=graph[0][0]
    
    while q:
        cost,x,y=heapq.heappop(q)
        
        # 현재 노드가 이미 처리된적 있다면
        if distance[x][y]<cost:
            continue
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            # 범위 채크
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            
            new_cost= cost+graph[nx][ny]
            if new_cost<distance[nx][ny]:
                distance[nx][ny]=new_cost
                heapq.heappush(q,(new_cost,nx,ny))
    return distance[N-1][N-1]


N=int(input())
while N!=0:
    graph=[]
    for i in range(N):
        graph.append(list(map(int,input().split())))
    print(f"Problem {count}: {dijackstra(graph)}")
    N=int(input())