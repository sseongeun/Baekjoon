import heapq,sys
input=sys.stdin.readline

INF=int(1e9)
V,E=map(int,input().split())
K=int(input())
graph=[[] for _ in range(V+1)] 
distance=[INF]*(V+1)
for _ in range(E):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
        
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    
    while q:
        dist,now= heapq.heappop(q)
        
        if dist>distance[now]:
            continue
        
        for i in graph[now]:
            cost=dist+i[0]
            if distance[i[1]]>cost:
                distance[i[1]]=cost
                heapq.heappush(q,(cost,i[1]))
           
           
           
dijkstra(K)       
for i in range(1,V+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])