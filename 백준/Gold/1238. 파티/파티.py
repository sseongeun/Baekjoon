import heapq
INF=int(1e9)

def dijkstra(X):
    q=[]
    heapq.heappush(q,(0,X))
    distance=[INF]*(N+1)
    distance[X]=0

    while q:
        dist,now=heapq.heappop(q)
        if dist<distance[now]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance

N,M,X=map(int,input().split())
graph=[[] for _ in range(N+1)]


for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))


result=[]
fromX=dijkstra(X)

for i in range(1,N+1):
    if i==X:
        continue
    array=dijkstra(i)
    result.append(array[X]+fromX[i])
    
print(max(result))