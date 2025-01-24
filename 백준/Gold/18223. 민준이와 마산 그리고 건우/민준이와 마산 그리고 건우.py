import heapq

V,E,P=map(int,input().split())
INF=int(1e9)
graph=[[] for _ in range(V+1)]
distance=[INF]*(V+1)

for _ in range(E):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
# 다익스트라 함수
def dijkstra(start):
    distance=[INF]*(V+1)
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    
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

if dijkstra(1)[P]+dijkstra(P)[V]==dijkstra(1)[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")